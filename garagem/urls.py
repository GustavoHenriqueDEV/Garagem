from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, MotoViewSet, CarroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"motos", MotoViewSet)
router.register(r"carros", CarroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
