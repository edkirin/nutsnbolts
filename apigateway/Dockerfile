FROM python:3.9-slim

ARG INTERNAL_PORT
ARG WORKERS
ARG NUTS_HOST
ARG BOLTS_HOST

ENV \
    DOCKER_CONTAINER Yes \
    INTERNAL_PORT ${INTERNAL_PORT} \
    WORKERS ${WORKERS} \
    NUTS_HOST ${NUTS_HOST} \
    BOLTS_HOST ${BOLTS_HOST} \
    TIMEZONE=Europe/Zagreb \
    PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN \
    ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
    echo $TIMEZONE > /etc/timezone && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

WORKDIR /app
COPY ./apigateway /app/apigateway
COPY requirements.txt /app
COPY run.py /app
COPY run.sh /app

RUN \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt

EXPOSE $INTERNAL_PORT

ENTRYPOINT [ "/app/run.sh" ]
