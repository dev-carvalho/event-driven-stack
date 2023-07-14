#---
# Author: Marcos Antonio de Carvalho 
#  eMAil: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Microsserviço para tratamento 
#         do PAGAMENTO.
#---
# payment.py

import os
import time

# Configuração da Aplicação 
from worker.config import app, setup
from worker.eCommerce.log import setlog as log

##---------------------##
##  P A G A M E N T O  ##
##---------------------##

# Lógica para processar o pagamento
@app.task
def payment( id ):
    event = "Pagamento Efetuado"
    log.saga_logger.info(f"{'Action Event'.ljust(14)} :: {id} :: {event}")
    return event

# Lógica para reverter o processamento do pagamento
@app.task
def reverse_payment( id ):
    event = "Pagamento Revertido"
    log.saga_logger.info(f"{'Reversal Event'.ljust(14)} :: {id} :: {event}")
    return event
    
