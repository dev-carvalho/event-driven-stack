##
# Author: Marcos Antonio de Carvalho (maio/2023)
# Descr.: API Tasks define as Ações de processamento para
#         os Eventos a ser processados pelos workers.
##
# Disponibilidade e Confiabilidade
# Tratamento de Falhas no processamento do Celery
##-

import os
import time
import random

## from celery.utils.log import get_task_logger

from celery import Celery
from celery import chain

## Registro de LOG
## logger = get_task_logger(__name__)

# Configuração da Aplicação 
from worker.config import app
from worker.config import setup

##---------------##
##  CHAIN TASKS  ##
##---------------##

@app.task(
  max_retry=4,         # Tentará no máximo 4 vezes
  retry_backoff=10,    # Tempo entre Tentativa exponencial: 10s, 20s, 30s e 60s.
                       # 2 minutos (120 segundos) tentando processar
)
def a(x):
  return x * 4

@app.task(
  max_retry=4,         # Tentará no máximo 4 vezes
  retry_backoff=10,    # Tempo entre Tentativa exponencial: 10s, 20s, 30s e 60s.
                       # 2 minutos (120 segundos) tentando processar
)
def b(x,y):
  return x + y

@app.task(
  #name='pipeline',     # Nome da task
  max_retry=4,         # Tentará no máximo 4 vezes
  retry_backoff=10,    # Tempo entre Tentativa exponencial: 10s, 20s, 30s e 60s.
                       # 2 minutos (120 segundos) tentando processar
)
def c():
  # é um pipeline. 
  # O .s é de sequence, ou seja: sequência.
  chain(a.s(1), b.s(2))
  # result = chain(a.s(1), b.s(2))
  # return result
  #
  # b(a(1),2)  
  # É um pipeline! Veja que o resultado da primeira 
  # função entra como parametro na segumda função.
  #
  # Tolerância a falhas:
  # Cada uma das função vai repetir, se precisar ser 
  # alguma falha repetida.





