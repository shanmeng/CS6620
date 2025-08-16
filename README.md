Name: Shan Meng
Date: August 15, 2025
Class: CS6620, Summer
Notes: Final Project



# PackMyBag API
This project is a RESTful API designed to generate and manage travel packing lists. based on your:
- Destination
- Trip duration
- Traveling with kids and/or pets

## Features
It features a cloud-native architecture where the backend infrastructure on AWS (S3 and DynamoDB) is fully managed by Terraform. The project includes a complete CI/CD pipeline using GitHub Actions that automatically provisions temporary cloud resources to run a full integration test suite.

- Fully RESTful: Supports "GET", "POST", "PUT", "DELETE".
- It now integrates with DynamoDB for storing data and S3 for archiving list contents.
- API endpoints
| Method | Endpoint                   | Description                      |
|--------|----------------------------|----------------------------------|
| POST   | `/lists`                   | Generate and save a packing list |
| GET    | `/lists/<list_id>`         | Retrieve a saved list            |
| PUT    | `/lists/<list_id>`         | Update an existing list          |
| DELETE | `/lists/<list_id>`         | Delete a saved list              |
| GET    | `/lists`                   | List all saved list IDs          |

## Project structures
```
pack-my-bag-api/
├── api.py                     # Flask API
├── PackMyBag.py               # Packing suggestion logic
├── requirements.txt           # Dependencies
├── test_api.py                # Pytest test cases
├── Dockerfile.api             # Docker build instructions for the main API container
├── Dockerfile.test            # Docker build instructions for running tests in a container
├── docker-compose.yml         # Orchestrates the API, Localstack (mock AWS), etc. for development
├── docker-compose.test.yml    # Orchestrates everything needed for running tests
├── run.sh                     # Start the development stack by calling docker-compose.yml
├── test.sh                    # Run tests and exit with success/failure status
├── .github/workflows/test.yml # GitHub Actions workflow
├── Iac/main.tf                # Terraform Infrastructure as Code files
└── README.md                  # You're here!
```

## Set up and how to use
1. Clone the repository.
```
bash

git clone https://github.com/shanmeng/CS6620.git
```

2. Navigate into the project directory.
```
bash

cd CS6620
```

3. Configure AWS credentials.
To ensure the local AWS CLI is configured with the necessary credentials, run.
```
bash

aws configure
```
Click Enter to confirm your AWS Access Key ID, Secret Access Key, and region name. 
```
bash
AWS Access Key ID [********************]: 
AWS Secret Access Key [********************]: 
Default region name [us-east-1]: 
Default output format [None]: 
```

4. Create the cloud infrastructure.
```
bash

cd Iac
terraform init
terraform apply
cd ..
```

5. Run the local application.
Export AWS credentials for Docker Compose:
```
bash

export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)
export AWS_REGION="us-east-1"
```
Export the resource names created by Terraform:
```
bash

export DYNAMODB_TABLE=$(terraform -chdir=Iac output -raw ddb_table)
export S3_BUCKET=$(terraform -chdir=Iac output -raw s3_bucket)
```
Start the application:
```
bash

docker compose up --build
```

6. Now the API is running at http://localhost:5050/lists.

7. Clean up infrastructure.
```
bash

terraform -chdir=Iac destroy
```


## Requirements
All dependencies are defined in requirements.txt and included in Docker containers.


## AI Assistance / External Tools Used
This project utilized AI assistance for debugging and clarifying concepts.

Tool used: Google Gemini, GitHub Copilot, ChatGPT

Prompts:
- "Can you help troubleshoot LocalStack errors?"
- "How can I wait for LocalStack to become healthy in a Docker Compose test container?"
- "How to fix 'ERROR: for test Container '...'' in Docker Compose with LocalStack health checks?"
- "Please find a solution for this failing job. Use the logs, job definition, and any referenced files where the failure occurred. Keep your response focused on the solution and include code suggestions when appropriate."

All AI-generated responses were reviewed and modified by me.
