from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Articulo(models.Model):

    class Meta:
        verbose_name_plural = "Artículos"

    titulo = models.CharField(max_length = 200)
    subtitulo = models.CharField(max_length = 200)
    cuerpo = models.CharField(max_length = 3000)
    autor = models.CharField(max_length = 40)
    fecha = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to="media/img-publicaciones/", null=True, blank=True)

    def __str__(self):
        return self.titulo
        
    
    


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)