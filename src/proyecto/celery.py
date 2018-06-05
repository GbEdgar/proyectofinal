from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

#Configurar con el mismo ambient que wsgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")
app = Celery('proj')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()

#tareas agendadas
app.conf.beat_schedule = {
    'app-every-5-seconds':{
        'task':'Envio_Recibo',
        'schedule':5.0,
        'args':('9172642325','Recibido','$10000')},
    'app-every-10-seconds':{
        'task':'Envio_Recibo',
        'schedule':10.0,
        'args':('2454363637','No_Recibido','$500')},
    'app-every-15-seconds':{
        'task':'Envio_Recibo',
        'schedule':15.0,
        'args':('6346574745','Recibido','$7800')},
    }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
#Tarea que es @app Unidad 3
