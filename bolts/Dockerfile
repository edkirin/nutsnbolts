FROM python:3.9-slim

ENV DOCKER_CONTAINER Yes

ARG INTERNAL_PORT
ARG WORKERS

ENV INTERNAL_PORT ${INTERNAL_PORT}
ENV WORKERS ${WORKERS}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./bolts /app/bolts
COPY requirements.txt /app
COPY run.py /app
COPY run.sh /app

RUN \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt

EXPOSE $INTERNAL_PORT

ENTRYPOINT [ "/app/run.sh" ]
