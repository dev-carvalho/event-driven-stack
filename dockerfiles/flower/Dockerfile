
##
# Inspiração
#   Repositório Oficial: docker-library/celery
#   https://github.com/docker-library/celery
#
# Ajustei o Dockerfile !!!
#
#   https://www.blueshoe.io/blog/strategies-for-slim-docker-images
##

##-------------------------##
##  M U L T I - S T A G E  ##
##-------------------------## 

FROM python:alpine as base
# Python 3.11.3
# pip 22.3.1
# celery 5.2.7 (dawn-chorus)

LABEL maintainer="Marcos Antônio de Carvalho <mrcos.antonio.carvalho@gmail.com>"
LABEL description="Docker container with the Flower."

# Setting para PYTHON
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH $PATH:/home/user/.local/bin/

# Atualiza o sistema e o pip (pip 23.0.1 --> pip 23.1.2)
RUN apk update && pip  --no-cache-dir install -U setuptools pip

# Add a user with an explicit UID/GID and create necessary directories
RUN set -eux; \
    addgroup -g 1000 user; \
    adduser  -u 1000 -G user user -D; 

# Usuário Default  
USER user

# Diretório do usuário
WORKDIR /home/user

##---------------------------##
##  2a fase - REQUERIMENTOS  ##
##  COMPILAÇÃO E CONSTRUÇÃO  ##
##---------------------------##
FROM base as builder

# Lista dos requisitos minimos
COPY --chown=1000:1000 dockerfiles/flower/requirements /code/requirements

# Instalando as dependencias para gerar um cache
RUN pip install --no-cache-dir --upgrade -r /code/requirements
