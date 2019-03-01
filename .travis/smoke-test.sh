#!/bin/bash
set -e

function finish {
    docker-compose --file docker/docker-compose.yml logs
    # TODO: deal with signal in app container for a faster and safer shutdown
    docker-compose --file docker/docker-compose.yml down --volumes
}

trap finish EXIT

docker-compose --file docker/docker-compose.yml up -d

# TODO: add healthcheck to container image
#.travis/docker-wait-healthy search_app_1

ping=$(curl -sS http://localhost:8080/ping 2>&1)
[[ "$ping" == "pong" ]]
