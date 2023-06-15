#---
# Author: Marcos Antonio de Carvalho (maio/2023)
# Descr.: API Tasks define as Ações de processamento para
#         os Eventos a ser processados pelos workers.
#---
# Disponibilidade e Confiabilidade
# Tratamento de Falhas no processamento do Celery
#--

##---------------------------------------##
##  TOO LONG - Processamentos DEMORADOS  ##
##---------------------------------------##

import os
import time
import random

## import celery_config
## from celery.utils.log import get_task_logger
from celery import Celery

app = Celery(
  'longs',  # Este arquivo com os processamentos
  broker="pyamqp://owl:owl@rabbitmq"
  # backend="amqp://owl:owl@rabbitmq",  
)

@app.task(
  queue='long_queue', # Fila de destino da task
  max_retry=4,        # Tentará no máximo 4 vezes
  retry_backoff=10,   # Tempo entre Tentativa exponencial: 10s, 20s, 30s e 60s.
                      # 2 minutos (120 segundos) tentando processar
 )
# Serie de Fibonacci
def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n-1) + fib(n-2)

@app.task(
  name='Meu teste',   # Nome da task 
  queue='long_queue', # Fila de destino da task
 # max_retry=4,       # Tentará no máximo 4 vezes
 # retry_backoff=10,  # Tempo entre Tentativa exponencial: 10s, 20s, 30s e 60s.
                      # 2 minutos (120 segundos) tentando processar
 )
def time_long(name):
    helloworld = 'Test Time {}'.format(name)
    try:
        time.sleep(60)
    except:
        time.sleep(60)
    return helloworld 

