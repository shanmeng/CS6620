#!/bin/bash
set -e

echo "Starting test stack using docker-compose.test.yml ..."
docker-compose -f docker-compose.test.yml up --build -d

echo "Waiting for LocalStack to be healthy on port 4567..."
until curl -sf http://localhost:4567/_localstack/health > /dev/null; do
  sleep 2
done
echo "LocalStack is ready!"

echo "Running tests..."
docker-compose -f docker-compose.test.yml logs -f test || true

echo "Cleaning up test stack ..."
docker-compose -f docker-compose.test.yml down -v

echo "Cleaning up leftover localstack directory ..."
fuser -k /tmp/localstack || true
rm -rf /tmp/localstack || true
