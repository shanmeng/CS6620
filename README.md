Name: Shan Meng
Date: June 25, 2025
Class: CS6620, Summer
Notes: Updated, CI/CD Pipeline Part 2



# PackMyBag API
This is a simple Flask-based API that generates travel packing suggestions based on your:
- Destination
- Trip duration
- Traveling with kids and/or pets


## Features
- Fully RESTful: Supports 'GET', 'POST', 'PUT', 'DELETE'.
- Includes: In-memory data storage, automated tests via pytest, CI/CD workflow with Github Actions, Dockerized setup for API and test environments


## Project structures
```
pack-my-bag-api/
├── api.py                 # Flask API
├── PackMyBag.py           # Packing suggestion logic
├── test_api.py            # Pytest test cases
├── requirements.txt       # Dependencies
├── Dockerfile.api         # Docker image for API
├── Dockerfile.test        # Docker image for running tests
├── run.sh                 # Start API in container
├── test.sh                # Run tests in container
├── .github/workflows/
│   └── python-app.yml     # GitHub Actions workflow
└── README.md              # You're here!
```

## Installation 
1. Clone the repository.
```
bash

git clone https://github.com/shanmeng/CS6620.git
cd CS6620
```
2. Install dependencies.
```
bash

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run the API locally.
```
bash

python.api.py
```
The server will be available at `http://localhost:5050`.


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


## Docker
Build and run the API container:
```
bash

./run.sh
```
Open: http://localhost:5050


## API endpoints
| Method | Endpoint                   | Description                      |
|--------|----------------------------|----------------------------------|
| POST   | `/lists`                   | Generate a packing list          |
| GET    | `/lists/<list_id>`         | Retrieve a saved list            |
| PUT    | `/lists/<list_id>`         | Update an existing list          |
| DELETE | `/lists/<list_id>`         | Delete a saved list              |
| GET    | `/lists`                   | List all saved list IDs          |


## Github Actions
This project includes an automated GitHub Actions workflow, every push to `main` runs:
- Dependency installation
- Unit tests via Pytest
Workflow file: `.github/workflows/python-app.yml`
Test results are viewable under the Actions tab on the repository page.


## Example: POST a JSON to the API
```
bash

curl -X POST http://localhost:5000/lists \
  -H "Content-Type: application/json" \
  -d '{"destination": "paris", "duration": 5, "weather": "cold"}'
```
This sends a POST request with JSON data to the Flask API.
