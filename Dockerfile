# Dockerfile that builds the python container for the application 

FROM python:3.7

ENV PYTHONBUFFERED 1 

RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    apt-utils

RUN mkdir /src
WORKDIR /src

ADD requirements.txt /src/

RUN pip install -r requirements.txt

ADD . /src/