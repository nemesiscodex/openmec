# import the logging library
import logging
from rest_framework.pagination import PaginationSerializer
from django.contrib.sites.models import get_current_site
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from openmec.forms import UploadFileForm
from openmec.models import *
from openmec.serializers import *
from django.contrib.auth.decorators import login_required


from openmec.utils import *
# Get an instance of a logger

logger = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def funcionario_list(request, anio, mes):

    documento = request.GET.get('documento')
    nombre = request.GET.get('nombre')

    mes = next(value for value, name in MES if name == mes)
    funcionarios = Funcionario.objects.all()
    if documento is not None:
        funcionarios = funcionarios.filter(documento=documento)
    if nombre is not None:
        funcionarios = funcionarios.filter(funcionario__icontains=nombre)
    page = request.GET.get('page')
    size = request.GET.get('size')
    if type(size) != type(0):
        size = 5

    request.session['anio'] = anio
    request.session['mes'] = mes

    paginator = Paginator(funcionarios, size)
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        funcionarios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        funcionarios = paginator.page(paginator.num_pages)
    # serializer = FuncionarioSerializer(funcionarios, many=True)
    serializer = PaginatedFuncionarioSerializer(funcionarios, context={'request': request})
    return JSONResponse(serializer.data)

def funcionario(request, documento, anio, mes):
    try:

        mes = next(value for value, name in MES if name == mes)
        funcionario = Funcionario.objects.get(documento=documento, anio=anio, mes=mes)
    except Funcionario.DoesNotExist:
        return HttpResponse(status=404)
    serializer = FuncionarioSerializer(funcionario)
    return JSONResponse(serializer.data)


def objeto_gasto_list(request):

    objeto_gasto = ObjetoGasto.objects.all()
    serializer = ObjetoGastoSerializer(objeto_gasto, many=True)
    return JSONResponse(serializer.data)


def objeto_gasto(request, codigo):
    try:
        objeto_gasto = ObjetoGasto.objects.get(codigo=codigo)
    except ObjetoGasto.DoesNotExist:
        return HttpResponse(status=404)
    serializer = ObjetoGastoSerializer(objeto_gasto)
    return JSONResponse(serializer.data)


def rubro(request, codigo, anio, mes):
    try:

        mes = next(value for value, name in MES if name == mes)
        rubro = Rubro.objects.get(codigo=codigo, anio=anio, mes=mes)
    except Rubro.DoesNotExist:
        return HttpResponse(status=404)
    serializer = RubroSerializer(rubro)
    return JSONResponse(serializer.data)


def dependencia_list(request):
    dependencia = Dependencia.objects.all()
    serializer = DependenciaSerializer(dependencia, many=True)
    return JSONResponse(serializer.data)


def cargo_list(request):
    cargo = Cargo.objects.all()
    serializer = CargoSerializer(cargo, many=True)
    return JSONResponse(serializer.data)


def rubro_list(request, anio, mes):

    mes = next(value for value, name in MES if name == mes)
    rubro = Rubro.objects.all().filter(anio=anio, mes=mes)
    serializer = RubroSerializer(rubro, many=True)
    return JSONResponse(serializer.data)


def concepto_list(request, anio, mes):

    mes = next(value for value, name in MES if name == mes)
    concepto = Concepto.objects.all().filter(anio=anio, mes=mes)
    serializer = ConceptoSerializer(concepto, many=True)
    return JSONResponse(serializer.data)


def home(request):
    urls = {}
    anios = [2014]
    meses = ['junio', 'julio', 'agosto']
    urls['funcionario'] = []
    urls['objeto_gasto'] = []
    urls['rubro'] = []
    urls['concepto'] = []
    for anio in anios:
        for mes in meses:
            urls['funcionario'].append('http://'+get_current_site(request).domain+reverse('funcionario_list',
                                                                                          kwargs={'anio': anio,
                                                                                                  'mes': mes}))

    urls['rubro'].append('http://'+get_current_site(request).domain+reverse('rubro_list'))
    urls['concepto'].append('http://'+get_current_site(request).domain+reverse('concepto_list'))
    urls['objeto_gasto'] = 'http://'+get_current_site(request).domain+reverse('objeto_gasto_list')
    urls['dependencia'] = 'http://'+get_current_site(request).domain+reverse('dependencia_list')
    urls['cargo'] = 'http://'+get_current_site(request).domain+reverse('cargo_list')

    return JSONResponse(urls)

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.POST.get('title'))
            return HttpResponseRedirect(home)
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',  context_instance=RequestContext(request, {'form': form}))


def save_wrapper(filename):

    try:
        data_save(filename)
    except Exception as e:
        logger.error("The csv file {0} could not be saved.".format(filename))
        logger.error(e)
    else:
        logger.info("The file was saved")


@login_required
def files(request):
    message = ''
    if request.method == 'POST':
        filename = request.POST.get('filename')
        save_wrapper(filename)
        # thread_csv = Thread(target=save_wrapper, args=(filename,))
        # thread_csv.start()
        message = 'Procesando Archivo.'
    file_list = get_file_list()
    for_all_files(file_list)
    file_list = get_file_list()
    return render_to_response('files.html',  context_instance=RequestContext(request, {'file_list': file_list,
                                                                                       'message':message}))