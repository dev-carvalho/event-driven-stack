

import os

from celery import Celery

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_USERNAME = os.getenv('REDIS_USERNAME', '')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'password')

AMQP_HOST = os.getenv('AMQP_HOST', 'localhost')
AMQP_PORT = int(os.getenv('AMQP_PORT', '5672'))
AMQP_USERNAME = os.getenv('AMQP_USERNAME', 'user')
AMQP_PASSWORD = os.getenv('AMQP_PASSWORD', 'password')

app_xxxx= Celery(
    'worker',
    #backend='redis://%s:%s@%s:%d/0' % (
    #    REDIS_USERNAME,
    #    REDIS_PASSWORD,
    #    REDIS_HOST,
    #    REDIS_PORT
    #),
    broker='pyamqp://%s:%s@%s:%d//' % (
        AMQP_USERNAME,
        AMQP_PASSWORD,
        AMQP_HOST,
        AMQP_PORT
    )
)

#app.conf.task_routes = {
#    'app.worker.celery_worker.test_celery': 'test-queue'}

#app.conf.update(task_track_started=True)



# Inicialize o objeto Celery
app = Celery(
  'owl',
   broker="amqp://owl:owl@rabbitmq",
   backend="rpc://",
   include=["owl.tasks",],
)

