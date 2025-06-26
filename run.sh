#!/bin/bash
echo "Building API container..."
docker build -f Dockerfile.api -t packmybag-api .

echo "Running API container on http://localhost:5000 ..."
docker run -p 5050:5000 packmybag-api


