# Author: Marcos Antonio de Carvalho (marcos.antonio.carvalho@gmail.com)
# Descr.: Configuração do Celery e do acesso ao Message Broker
#---
# config.py

#
# https://docs.celeryq.dev/en/stable/userguide/configuration.html
#

#import os 
#BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://')

## Broker settings.
#broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
#imports = ('myapp.tasks',)


import os
from celery import Celery

#app.conf.task_routes = {
#    'app.worker.celery_worker.test_celery': 'test-queue'}

#app.conf.update(task_track_started=True)

# Objeto/Classe de Configuração.
class Config:
    enable_utc = True
    timezone   = 'America/Sao_Paulo'
    # Configura a comunicação DEFAULT
    task_default_queue         = "default_queue"
    task_default_exchange      = "default_queue"
    task_default_exchange_type = "direct"
    task_default_routing_key   = "default"
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_create_missing_queues
    # Se habilitado (padrão), qualquer fila especificada que não esteja definida
    # em task_queues será criada automaticamente.
    task_create_missing_queues = "disable"
    # https://docs.celeryq.dev/en/stable/userguide/routing.html
    task_routes = ([
        ('worker.tasks.default.*', {'queue': 'default_queue'}),
        ('worker.tasks.long.*',    {'queue': 'long_queue'}),
        ('worker.scheduler.*',     {'queue': 'schedule_queue'}),
    ],) 


# Inicialize o objeto Celery
app = Celery(
  'app',
   broker="pyamqp://owl:owl@rabbitmq",
   backend="rpc://",
   # include=["owl.tasks",],
)

# Configura a aplicação apartir do objeto/classe de configuração.
app.config_from_object(Config)

# Define a function
def world():
    print("Hello, World!")