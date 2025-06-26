#!/bin/bash
echo "Building test container..."
docker build -f Dockerfile.test -t packmybag-test .

echo "Running tests..."
docker run --rm packmybag-test
