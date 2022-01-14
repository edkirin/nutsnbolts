#!/bin/sh

export DOCKER_CONTAINER="${DOCKER_CONTAINER:=No}"
export INTERNAL_PORT="${INTERNAL_PORT:=5001}"
export WORKERS="${WORKERS:=2}"
export DB_HOST="${DB_HOST:=localhost}"
export DB_PORT="${DB_PORT:=55432}"
export DB_NAME="${DB_NAME:=nutsnbolts}"
export DB_USER="${DB_USER:=nutsnbolts}"
export DB_PASSWORD="${DB_PASSWORD:=nutsnbolts}"

echo "---------------------------------"
echo "Using environment:"
echo "    DOCKER_CONTAINER: $DOCKER_CONTAINER"
echo "    INTERNAL_PORT:    $INTERNAL_PORT"
echo "    WORKERS:          $WORKERS"
echo "    DB_HOST:          $DB_HOST"
echo "    DB_PORT:          $DB_PORT"
echo "    DB_NAME:          $DB_NAME"
echo "    DB_USER:          $DB_USER"
echo "    DB_PASSWORD:      $DB_PASSWORD"
echo "---------------------------------"

uvicorn \
    run:app \
    --host 0.0.0.0 \
    --port $INTERNAL_PORT \
    --workers=$WORKERS
