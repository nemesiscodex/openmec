from django.db import transaction
from openmec import settings
import os
from openmec.models import *


def handle_uploaded_file(f, title):
    with open(title+'.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open(title+'.csv', 'r+') as source:
        for line in source:
            print line.replace('\n','').split(";")

def get_file_list():
    return [file for file in os.listdir(os.path.join(settings.BASE_DIR,'csv')) if file.endswith('.csv')]


def load_data(filename):
    with open('csv/'+filename, 'r+') as csv_file:
        for line in csv_file:
            row = line.replace('\n', '')

@transaction.atomic
def data_save(filename):
    """
    save the data from a csv file to the database
    :param filename:
    :return:
    """
    with open(os.path.join(os.path.join(settings.BASE_DIR, 'csv'), filename), 'r+') as csv_file:
        first = True
        for line in csv_file:
            if not first:
                row = line.replace('\n', '').replace('\"', '').split(';')
                #print(row)
                mes = next(value for value, name in MES if name == row[0].strip())

                anio = int(row[1].strip())
                documento = row[2].strip()
                funcionario = row[3].strip()

                #crear objeto gasto
                objeto_gasto = row[4].strip().replace(')','').split('(')
                objeto_gasto_nombre = objeto_gasto[0].strip()
                objeto_gasto_codigo = objeto_gasto[1].strip()
                objeto_gasto_bd = None
                if objeto_gasto_codigo != '':
                    if ObjetoGasto.objects.filter(codigo=objeto_gasto_codigo).exists():
                        objeto_gasto_bd = ObjetoGasto.objects.get(codigo=objeto_gasto_codigo)
                    else:
                        objeto_gasto_bd = ObjetoGasto()
                        objeto_gasto_bd.codigo = objeto_gasto_codigo
                        objeto_gasto_bd.nombre = objeto_gasto_nombre
                        objeto_gasto_bd.save()

                estado = row[5].strip()
                antiguedad = row[6].strip()


                #crear objeto dependencia
                dependencia = row[8].strip()
                dependencia_bd = None
                if dependencia != '':
                    if Dependencia.objects.filter(institucion=dependencia).exists():
                        dependencia_bd = Dependencia.objects.get(institucion=dependencia)
                    else:
                        dependencia_bd = Dependencia()
                        dependencia_bd.institucion = dependencia
                        dependencia_bd.save()


                cargo = row[9].strip()
                cargo_bd = None
                if cargo != '':
                    if Cargo.objects.filter(cargo=cargo).exists():
                        cargo_bd = Cargo.objects.get(cargo=cargo)
                    else:
                        cargo_bd = Cargo()
                        cargo_bd.cargo = cargo
                        cargo_bd.save()

                nro_matricula = row[10].strip()
                if nro_matricula == '':
                    nro_matricula = 0
                else:
                    nro_matricula = int(nro_matricula)

                # crear objeto funcionario
                if Funcionario.objects.filter(documento=documento).exists():
                    funcionario_bd = Funcionario.objects.get(documento=documento)
                else:
                    funcionario_bd = Funcionario()
                    funcionario_bd.documento = documento
                    funcionario_bd.funcionario = funcionario
                    funcionario_bd.nro_matriculacion = nro_matricula
                    funcionario_bd.save()

                # crear objeto rubro
                rubro = row[11].strip()
                monto_rubro = row[12].strip()
                rubro_bd = None
                if rubro != '':
                    if Rubro.objects.filter(codigo=rubro).exists():
                        rubro_bd = Rubro.objects.get(codigo=rubro)
                    else:
                        rubro_bd = Rubro()
                        rubro_bd.codigo = rubro
                        rubro_bd.monto = int(monto_rubro)
                        rubro_bd.save()

                cantidad = int(row[13].strip())
                asignacion = int(row[14].strip())

                # crear objeto concepto
                concepto = row[7].strip()
                concepto_bd = None
                if concepto != '':
                    if Concepto.objects.filter(concepto=concepto).exists():
                        concepto_bd = Concepto.objects.get(concepto=concepto)
                        if concepto_bd.maximo < asignacion:
                            concepto_bd.maximo = asignacion
                        if concepto_bd.minimo > asignacion:
                            concepto_bd.minimo = asignacion
                        concepto_bd.promedio = (concepto_bd.promedio + float(asignacion)) / 2.0
                        concepto_bd.save()
                    else:
                        concepto_bd = Concepto()
                        concepto_bd.concepto = concepto
                        concepto_bd.minimo = asignacion
                        concepto_bd.maximo = asignacion
                        concepto_bd.promedio = asignacion
                        concepto_bd.save()


                # crear objeto datos
                if Datos.objects.filter(mes=mes, anio=anio, funcionario=funcionario_bd, objeto_gasto=objeto_gasto_bd,
                                        concepto=concepto_bd, dependencia=dependencia_bd, cargo=cargo_bd,
                                        rubro=rubro_bd).exists():
                    pass
                else:
                    datos_bd = Datos()
                    datos_bd.mes = mes
                    datos_bd.anio = anio
                    datos_bd.funcionario = funcionario_bd
                    datos_bd.estado = estado
                    datos_bd.objeto_gasto = objeto_gasto_bd
                    datos_bd.concepto = concepto_bd
                    datos_bd.dependencia = dependencia_bd
                    datos_bd.cargo = cargo_bd
                    datos_bd.rubro = rubro_bd
                    datos_bd.save()

            else:
                first = False