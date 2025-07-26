#!/bin/bash
set -e

echo "Running test stack using docker-compose.test.yml ..."
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit

echo "Cleaning up test stack ..."
docker-compose -f docker-compose.test.yml down -v
fuser -k /tmp/localstack || true
rm -rf /tmp/localstack
