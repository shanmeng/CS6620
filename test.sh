#!/bin/bash
echo "Running test stack using docker-compose.test.yml ..."
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
STATUS=$?

# Clean up containers
docker-compose -f docker-compose.test.yml down

exit $STATUS