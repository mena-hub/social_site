from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor import fields

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="título")
    content = fields.RichTextField(verbose_name="contenido")
    ordering = models.SmallIntegerField(default=0, verbose_name="orden")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['ordering', 'title']

    def __str__(self):
        return self.title

    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('pages:page', kwargs={'pk': self.id, 'slug': self.get_slug()})
