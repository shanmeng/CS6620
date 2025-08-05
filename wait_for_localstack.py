import os
import time
import requests
import sys

endpoint = os.getenv(\"DYNAMODB_ENDPOINT\", \"http://localstack:4566\")
print(f\"Waiting for LocalStack DynamoDB and S3 at {endpoint}...\")
        
max_attempts = 40 # 40 * 5s = 200s wait
attempts = 0
while attempts < max_attempts:
    try:
        response = requests.get(f\"{endpoint}/_localstack/health?services=s3,dynamodb\", timeout=5)
        response.raise_for_status()
        health_data = response.json().get(\"services\", {})
        s3_status = health_data.get(\"s3\")
        dynamodb_status = health_data.get(\"dynamodb\")

        # TA's feedback: Update check for "available" and "running" statuses
        if s3_status in [\"running\", \"available\"] and dynamodb_status in [\"running\", \"available\"]:
            print(\"LocalStack S3 and DynamoDB are running!\")
            sys.exit(0)
        else:
            print(f\"LocalStack nOT ready. S3: {s3_status}, DynamoDB: {dynamodb_status}\")
    except requests.exceptions.RequestException as e:
        print(f\"Error: {e}\")

    time.sleep(5)
    attempts += 1

print(\"LocalStack services did not become healthy in time after multiple attempts. Exiting.\")
sys.exit(1)
