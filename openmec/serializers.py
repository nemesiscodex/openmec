
from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
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

    datos = serializers.SerializerMethodField('get_datos')
    # datos = DatosSerializer(many=True, blank=True)

    def get_datos(self, obj):
        session = self.context['request'].session
        anio = int(session['anio'])
        mes = session['mes']
        datos = Datos.objects.filter(funcionario=obj, mes=mes, anio=anio)
        serializer = DatosSerializer(datos, many=True, blank=True)
        return serializer.data

    class Meta:
        model = Funcionario
        fields = ('documento', 'funcionario', 'nro_matriculacion', 'datos')


class PaginatedFuncionarioSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = FuncionarioSerializer