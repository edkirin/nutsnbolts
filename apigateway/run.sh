#!/bin/sh

export DOCKER_CONTAINER="${DOCKER_CONTAINER:=No}"
export INTERNAL_PORT="${INTERNAL_PORT:=5000}"
export WORKERS="${WORKERS:=2}"
export NUTS_HOST="${NUTS_HOST:=http://nuts-n-bolts:5001}"
export BOLTS_HOST="${BOLTS_HOST:=http://nuts-n-bolts:5002}"

echo "---------------------------------"
echo "Using environment:"
echo "    DOCKER_CONTAINER: $DOCKER_CONTAINER"
echo "    INTERNAL_PORT:    $INTERNAL_PORT"
echo "    WORKERS:          $WORKERS"
echo "    NUTS_HOST:        $NUTS_HOST"
echo "    BOLTS_HOST:       $BOLTS_HOST"
echo "---------------------------------"

uvicorn \
    run:app \
    --host 0.0.0.0 \
    --port $INTERNAL_PORT \
    --workers=$WORKERS
