FROM postgres:14-bullseye

ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

ENV \
    PGDATABASE ${POSTGRES_DB} \
    PGUSER ${POSTGRES_USER} \
    PGPASSWORD ${POSTGRES_PASSWORD}

#RUN \
#    apt-get update && \
#    apt-get install wget -y && \
#    apt-get clean
#
#RUN \
#    wget -qO- \
#    https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/8.4.1/flyway-commandline-8.4.1-linux-x64.tar.gz | tar xvz && \
#    ln -s `pwd`/flyway-8.4.1/flyway /usr/local/bin && \
#    chmod 755 /flyway-8.4.1/flyway

WORKDIR /app
COPY ./sql /app/sql
#COPY flyway.conf /app
#COPY migrate.sh /docker-entrypoint-initdb.d
#COPY ./init_db.sql /docker-entrypoint-initdb.d
COPY ./sql/* /docker-entrypoint-initdb.d/
