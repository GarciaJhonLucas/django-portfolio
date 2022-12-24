from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Proyecto(models.Model):
    foto = models.ImageField(upload_to='portafolio/images')
    titulo = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)
    tags = models.CharField(max_length=250, blank=False)
    url_github = models.URLField(blank=False)
    
    def save(self, *args, **kwargs):
        return super(Proyecto, self).save(*args, **kwargs)


class Visitante(models.Model):
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip