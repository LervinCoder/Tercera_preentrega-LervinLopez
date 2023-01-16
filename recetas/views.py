from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import Usuario, Receta, Datos_curiosos


def bienvenida(request):
    contexto = {
    }
                
    return render(
      request=request, 
      template_name='recetas/inicio.html',
      context=contexto
      )

def listar_recetas(request):
    contexto = {
        'recetas': Receta.objects.all()

    }
    return render(
      request=request, 
      template_name='recetas/lista_recetas.html',
      context=contexto
      )


def listar_usuarios_destacados(request):
    contexto = {
        'usuarios' : Usuario.objects.all()
    }
    return render(
      request=request, 
      template_name='recetas/lista_usuarios_destacados.html',
      context=contexto
      )


def dato_curioso(request):
    contexto = {
        'dato_curioso' : Datos_curiosos.objects.all()
    
    }
    return render(
      request=request, 
      template_name='recetas/datos_curiosos.html',
      context=contexto
      )