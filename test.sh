#!/bin/bash
set -e

echo "Starting test stack using docker-compose.test.yml..."
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit

echo "Test finished. Cleaning up test stack..."
docker compose -f docker-compose.test.yml down -v

echo "Cleaning up leftover localstack directory..."
fuser -k /var/lib/localstack || true
rm -rf /var/lib/localstack || true

