from __future__ import unicode_literals

from django.db import models


#Create your models here
class SistemaPagoOnline(models.Model):
    item_name = models.CharField(max_length=120, null=True, blank=True)
    pago_folio = models.CharField(max_length=120, null=True, blank=True)
    pago_articulo = models.CharField(max_length=120, null=True, blank=True)
    pago_total= models.CharField(max_length=120, null=True, blank=True)
    ticket_created = models.DateTimeField(auto_now_add = True)
    mensaje = models.CharField(max_length=120, null=True, blank =True)

    def __str__(self):
        return str(self.mensaje)
