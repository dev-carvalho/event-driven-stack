#---
# Author: Marcos Antonio de Carvalho (marcos.antonio.carvalho@gmail.com)
# Descr.: Carrega as Tasks do processamento online 
#         que seram executados pelos Workers DEFAULT.
#---
from celery import Celery

# Carrega as funções do processamento Online do Workers DEFAULT.
from worker.default.commons import *  # Funções Comuns
from worker.default.chains  import *  # Funções em Cadeia




