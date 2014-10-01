from django.db import models


class ObjetoGasto(models.Model):
    # "111"
    codigo = models.CharField(max_length=30,primary_key=True)
    # "Sueldo"
    nombre = models.CharField(max_length=128)


MES = (
    (1, 'enero'),
    (2, 'febrero'),
    (3, 'marzo'),
    (4, 'abril'),
    (5, 'mayo'),
    (6, 'junio'),
    (7, 'julio'),
    (8, 'agosto'),
    (9, 'setiembre'),
    (10, 'octubre'),
    (11, 'noviembre'),
    (12, 'diciembre'),
)



class Dependencia(models.Model):
    # This field may not exist in the pdf
    # "16014"
    # codigo = models.CharField(max_length=30, primary_key=True)

    # ESC. BAS. 295 PANAMERICANA
    institucion = models.CharField(max_length=128, primary_key=True)


class Cargo(models.Model):
    # This field may not exist in the pdf
    # "50420"
    # codigo = models.CharField(max_length=30, primary_key=True)

    # "Catedratico de Lengua Guarani"
    cargo = models.CharField(max_length=128)


class Rubro(models.Model):
    # "Z51"
    codigo = models.CharField(max_length=30, primary_key=True)
    # 16750
    monto = models.IntegerField()


class Concepto(models.Model):
    # "Sueldos"
    concepto = models.CharField(max_length=128, primary_key=True)
    # valor calculado
    minimo = models.IntegerField()
    # valor calculado
    maximo = models.IntegerField()
    # valor calculado
    promedio = models.FloatField()

class Funcionario(models.Model):
    # "123456"
    documento = models.CharField(max_length=30, primary_key=True)
    # "Juan Perez"
    funcionario = models.CharField(max_length=128)
    # 123415
    nro_matriculacion = models.IntegerField()
    class Meta:
        ordering = ('funcionario',)

class Datos(models.Model):
    id = models.AutoField(primary_key=True)
    # 8 (Agosto)
    mes = models.IntegerField(choices=MES)
    # 2014
    anio = models.IntegerField()
    funcionario = models.ForeignKey("Funcionario", related_name='datos')
    # "Permanente"
    estado = models.CharField(max_length=30)
    objeto_gasto = models.ForeignKey("ObjetoGasto", null=True, related_name='datos')
    concepto = models.ForeignKey("Concepto", null=True, related_name='datos')
    dependencia = models.ForeignKey("Dependencia", null=True, related_name='datos')
    cargo = models.ForeignKey("Cargo", null=True, related_name='datos')
    rubro = models.ForeignKey("Rubro", null=True, related_name='datos')
