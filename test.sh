#!/bin/bash
set -e

echo "Waiting for LocalStack to be healthy..."
until curl -sf http://localhost:4567/_localstack/health > /dev/null; do
  sleep 2
done
echo "LocalStack is ready!"


echo "Running test stack using docker-compose.test.yml ..."
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit

echo "Cleaning up test stack ..."
docker-compose -f docker-compose.test.yml down -v
fuser -k /tmp/localstack || true
rm -rf /tmp/localstack
