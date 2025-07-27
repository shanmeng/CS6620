Name: Shan Meng
Date: July 25, 2025
Class: CS6620, Summer
Notes: Updated, CI/CD Pipeline Part 3



# PackMyBag API
This project is a RESTful API designed to generate and manage travel packing lists. based on your:
- Destination
- Trip duration
- Traveling with kids and/or pets


## Features
- Fully RESTful: Supports "GET", "POST", "PUT", "DELETE".
- It now integrates with DynamoDB for storing data and S3 for archiving list contents.

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
└── README.md                  # You're here!
```


## Installation 
1. Clone the Repository.
```
bash

git clone https://github.com/shanmeng/CS6620.git
cd CS6620
```
2. Run the App with Docker Compose
```
bash

./run.sh
```
This launches the full stack: API + Localstack.
Once the stack is up, open your browser at: http://localhost:5050

3. API endpoints
| Method | Endpoint                   | Description                      |
|--------|----------------------------|----------------------------------|
| POST   | `/lists`                   | Generate and save a packing list |
| GET    | `/lists/<list_id>`         | Retrieve a saved list            |
| PUT    | `/lists/<list_id>`         | Update an existing list          |
| DELETE | `/lists/<list_id>`         | Delete a saved list              |
| GET    | `/lists`                   | List all saved list IDs          |


## Testing
1. Option 1: Run tests locally
```
bash

pytest test_api.py
```
2. Option 2: Run tests in Docker
```
bash

./test.sh
```


## CI/CD with GitHub Actions
This repo includes an automated Github Actions workflow at
```
bash

.github/workflows/test.yml
```
Every push to `main` will:
- Build the stack with Docker Compose, ensuring LocalStack services are ready.
- Run the full test suite against Localstack mock AWS environment.
Test results are viewable under the Actions tab on the repository page.


## Example: POST a JSON to the API
```
bash

curl -X POST http://localhost:5050/lists \
  -H "Content-Type: application/json" \
  -d '{"destination": "paris", "duration": 5, "weather": "cold"}'
```
This sends a POST request with JSON data to the Flask API.

## Requirements
All dependencies are defined in requirements.txt and included in Docker containers.



## AI Assistance / External Tools Used
This project utilized AI assistance for debugging and clarifying concepts.

Tool used: Google Gemini

Prompts:
- "Can you help troubleshoot LocalStack errors?"
- "How can I wait for LocalStack to become healthy in a Docker Compose test container?"
- "How to fix 'ERROR: for test Container '...'' in Docker Compose with LocalStack health checks?"
All AI-generated responses were reviewed and modified by me.
