from django.db import models

# Create your models here


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
