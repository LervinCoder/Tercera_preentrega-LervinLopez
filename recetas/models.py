from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=64)
    bio = models.TextField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    tiempo_de_preparacion = models.CharField(max_length=24)
    equipos_para_la_preparacion = models.CharField(max_length=256)
    ingredientes = models.CharField(max_length=512)
    consejos = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.nombre


class Datos_curiosos(models.Model):
    datos_curiosos = models.CharField(max_length=256)
    esta_buena_la_informacion = models.BooleanField(default=False)

    def __str__(self):
        return self.datos_curiosos



