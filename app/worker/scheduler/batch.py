##
# Author: Marcos Antonio de Carvalho (marcos.antonio.carvalho@gmail.com)
# Descr.: Configuração do acesso ao Message Broker e
#         das funções do processamento Batch.
#---
# batch.py

# Configuração da Aplicação 
from worker.config import app
from worker.config import setup

@app.task
def say(what):
    print(what)

    