from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo

    def __str__(self):
        return self.cano

    def __str__(self):
        return self.marca


class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="carros"
    )

    def __str__(self):
        return self.modelo

    def __str__(self):
        return self.ano

    def __str__(self):
        return self.marca


# Create your models here.
