from django.db import models

# Create your models here.
class Proyecto(models.Model):
    foto = models.ImageField(upload_to='portafolio/images')
    titulo = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)
    tags = models.CharField(max_length=250, blank=False)
    url_github = models.URLField(blank=False)