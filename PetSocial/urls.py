from django.contrib import admin
from django.urls import path
from pets.views import agregar_mascota
from pets.views import ver_servicios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agregar_mascota, name='agregar_mascota'),
    path('servicios/', ver_servicios, name='ver_servicios'),
]
