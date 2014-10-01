
from rest_framework import serializers
from openmec.models import *


class ObjetoGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoGasto
        fields = ('codigo', 'nombre')


class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = ('institucion',)



class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo',)



class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = ('codigo', 'monto')


class ConceptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concepto
        fields = ('concepto', 'minimo', 'maximo', 'promedio')


class DatosSerializer(serializers.ModelSerializer):

    objeto_gasto = ObjetoGastoSerializer()
    concepto = ConceptoSerializer()
    dependencia = DependenciaSerializer()
    cargo = CargoSerializer()
    rubro = RubroSerializer()

    class Meta:
        depth = 1
        model = Datos
        fields = ('id', 'mes', 'anio', 'estado', 'objeto_gasto',
                  'concepto', 'dependencia', 'cargo', 'rubro')



class FuncionarioSerializer(serializers.ModelSerializer):
    datos = DatosSerializer(many=True, blank=True)
    class Meta:
        model = Funcionario
        fields = ('documento', 'funcionario', 'nro_matriculacion', 'datos')
