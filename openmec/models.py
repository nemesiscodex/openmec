from django.db import models


class ObjetoGasto(models.Model):
    # "111"
    codigo = models.CharField(max_length=30,primary_key=True)
    # "Sueldo"
    nombre = models.CharField(max_length=128)


MES = (
    (1, 'Enero'),
    (2, 'Febrero'),
    (3, 'Marzo'),
    (4, 'Abril'),
    (5, 'Mayo'),
    (6, 'Junio'),
    (7, 'Julio'),
    (8, 'Agosto'),
    (9, 'Setiembre'),
    (10, 'Octubre'),
    (11, 'Noviembre'),
    (12, 'Diciembre'),
)


class Datos(models.Model):
    id = models.AutoField(primary_key=True)
    # 8 (Agosto)
    mes = models.IntegerField(choices=MES)
    # 2014
    anio = models.IntegerField()
    funcionario = models.ForeignKey("Funcionario")
    # "Permanente"
    estado = models.CharField(max_length=30)
    objeto_gasto = models.ForeignKey("ObjetoGasto")
    concepto = models.ForeignKey("Concepto")
    dependencia = models.ForeignKey("Dependencia")
    cargo = models.ForeignKey("Cargo")
    rubro = models.ForeignKey("Rubro")



class Dependencia(models.Model):
    # "16014"
    codigo = models.CharField(max_length=30, primary_key=True)
    # ESC. BAS. 295 PANAMERICANA
    institucion = models.CharField(max_length=128)


class Cargo(models.Model):
    # "50420"
    codigo = models.CharField(max_length=30, primary_key=True)
    # "Catedratico de Lengua Guarani"
    cargo = models.CharField(max_length=128)


class Rubro(models.Model):
    # "Z51"
    codigo = models.CharField(max_length=30, primary_key=True)
    # 16750
    monto = models.IntegerField()


class Concepto(models.Model):
    # "1111000"
    codigo = models.CharField(max_length=30, primary_key=True)
    # "Sueldos"
    concepto = models.CharField(max_length=128)
    # valor calculado
    minimo = models.IntegerField()
    # valor calculado
    maximo = models.IntegerField()
    # valor calculado
    promedio = models.FloatField()

class Funcionario(models.Model):
    # "123456"
    documento = models.IntegerField(primary_key=True)
    # "Juan Perez"
    funcionario = models.CharField(max_length=128)
    # 123415
    nro_matriculacion = models.IntegerField(unique=True)