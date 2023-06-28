from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre, self.correo_electronico, self.contrasena, self.edad

class Juego(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre