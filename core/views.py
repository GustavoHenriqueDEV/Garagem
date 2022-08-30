from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Moto, Carro
from core.serializers import CategoriaSerializer, MotoSerializer, CarroSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


class MotoViewSet(ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
