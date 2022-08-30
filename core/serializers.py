from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Moto, Carro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MotoSerializer(ModelSerializer):
    class Meta:
        model = Moto
        fields = "__all__"


class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"
