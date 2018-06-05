from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import SistemaPagoOnline

@task(name="Envio_Recibo")
def email(folio, articulo, total):
    pago_folio = folio
    pago_articulo = articulo
    pago_total = total
    mensaje = folio, articulo, total
    new_obj = SistemaPagoOnline.objects.create(item_name='Recibo',
    pago_folio = pago_folio,
    pago_articulo = pago_articulo,
    pago_total = pago_total,
    mensaje = mensaje)
    return mensaje
