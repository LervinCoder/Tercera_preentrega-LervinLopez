from django.urls import path
from recetas.views import bienvenida, listar_recetas, listar_usuarios_destacados, dato_curioso


urlpatterns = [
    path('inicio/', bienvenida),
    path('listado-recetas/', listar_recetas),
    path('usuarios-destacados/', listar_usuarios_destacados),
    path('datos-curiosos/', dato_curioso)
]