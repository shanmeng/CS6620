#!/bin/bash
set -e

echo "Starting test stack using docker-compose.test.yml ..."
docker-compose -f docker-compose.test.yml up --build -d

echo "LocalStack should be ready based on docker-compose healthcheck."

echo "Running tests..."
docker-compose -f docker-compose.test.yml run --rm test

TEST_EXIT_CODE=$?

echo "Cleaning up test stack ..."
docker-compose -f docker-compose.test.yml down -v

echo "Cleaning up leftover localstack directory ..."
fuser -k /tmp/localstack || true
rm -rf /tmp/localstack || true

exit $TEST_EXIT_CODE
