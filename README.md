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
├── wait_for_localstack.py     # Utility script to ensure application waits until the localstack container is ready
├── run.sh                     # Start the development stack by calling docker-compose.yml
├── test.sh                    # Run tests and exit with success/failure status
├── .github/workflows/test.yml # GitHub Actions workflow
└── README.md                  # You're here!
```

## Set up and how to use
1. Clone the Repository.
```
bash

git clone https://github.com/shanmeng/CS6620.git
```

2. Navigate into the project directory.
```
bash

cd CS6620
```

3. Make the shell script executable.
This one-time step is required on macOS and Linux to give your system permission to run the scripts.
```
bash

chmod +x ./run.sh
chmod +x ./test.sh
```

4. Running the Application.
```
bash

./run.sh
```
The script uses docker-compose.yml to build and start the container.

5. Running the Test. Keep your current terminal running. Open a new terminal window and run the Test in the new window.
```
bash

./test.sh
```
The script uses docker-compose.test.yml to build a clean test environment, run all tests, and then automatically shut down the containers.

6. You can test the endpoint with curl in the new terminal window.
```
bash
curl -X POST http://localhost:5050/lists \
  -H "Content-Type: application/json" \
  -d '{"destination":"paris","duration":3,"weather":"cold","with_kids":true,"with_pet":false}'
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


## Requirements
All dependencies are defined in requirements.txt and included in Docker containers.



## AI Assistance / External Tools Used
This project utilized AI assistance for debugging and clarifying concepts.

Tool used: Google Gemini, GitHub Copilot.

Prompts:
- "Can you help troubleshoot LocalStack errors?"
- "How can I wait for LocalStack to become healthy in a Docker Compose test container?"
- "How to fix 'ERROR: for test Container '...'' in Docker Compose with LocalStack health checks?"
- "Please find a solution for this failing job. Use the logs, job definition, and any referenced files where the failure occurred. Keep your response focused on the solution and include code suggestions when appropriate."

All AI-generated responses were reviewed and modified by me.
