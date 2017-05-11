# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models


class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha = models.DateTimeField("Fecha de publicación")

    def fue_publicado_recientemente (self):
        return self.fecha >= timezone.now()- datetime.timedelta(days=1)

    fue_publicado_recientemente.admin_order_field = 'fecha'
    fue_publicado_recientemente.boolean = True
    fue_publicado_recientemente.short_description = '¿Es reciente?'

    def __unicode__(self): # __unicode__ en Python 2
        return self.texto_pregunta

    def publicado_recientemente(self):
        return self.fecha >= timezone.now()-datetime.timedelta(days=1)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'opción'# El nombre del modelo
        verbose_name_plural = 'opciones'# El nombre en plural

    def __unicode__(self): # __unicode__ en Python 2
        return self.texto_opcion

