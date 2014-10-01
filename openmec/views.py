# import the logging library
import logging
from threading import Thread

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.renderers import JSONRenderer
from openmec.forms import UploadFileForm
from openmec.models import *
from openmec.serializers import FuncionarioSerializer
from openmec.utils import handle_uploaded_file, get_file_list, data_save
from django.contrib.auth.decorators import login_required


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


def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    serializer = FuncionarioSerializer(funcionarios, many=True)
    return JSONResponse(serializer.data)


def objeto_gasto_list(request):
    objeto_gasto = ObjetoGasto.objects.all()
    serializer = FuncionarioSerializer(objeto_gasto, many=True)
    return JSONResponse(serializer.data)


def home(request):
    return render_to_response("home.html")

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
    return render_to_response('files.html',  context_instance=RequestContext(request, {'file_list': file_list,
                                                                                       'message':message}))