# Name: Shan Meng
# Date: July 25, 2025
# Class: CS6620
# Notes: Assignment CI/CD pipeline part 3


import pytest
import json
import os
import boto3
from api import app

# Use the Localstack endpoints
DYNAMODB_ENDPOINT = os.environ.get("DYNAMODB_ENDPOINT", "http://localhost:4566")
S3_ENDPOINT = os.environ.get("S3_ENDPOINT", "http://localhost:4566")
TABLE_NAME = os.environ.get("DYNAMODB_TABLE", "PackMyBagTable")
BUCKET_NAME = os.environ.get("S3_BUCKET", "packmybag-bucket")

# Pytest fixture to create a test client for the Flask app
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def get_dynamodb_item(item_id):
    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={"id": item_id})
    return response.get("Item")

# Helper function to retrieve object content from S3
def get_s3_object_content(item_id):
    s3 = boto3.client("s3", endpoint_url=S3_ENDPOINT)
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=f"{item_id}.json")
        return json.loads(obj["Body"].read())
    except:
        return None


# Test POST and check DynamoDB + S3
def test_post_and_get_list(client):
    payload = {
        "destination": "paris",
        "duration": 3,
        "weather": "cold",
        "with_kids": True,
        "with_pet": False
    }
    response = client.post("/lists", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    list_id = data["id"]
    
 	# Validate data is stored in both DB and S3
    db_item = get_dynamodb_item(list_id)
    s3_content = get_s3_object_content(list_id)
    assert db_item is not None
    assert s3_content is not None
    assert db_item["items"] == s3_content["items"]

	# Validate the GET request retrieves the data correctly
    get_response = client.get(f"/lists/{list_id}")
    assert get_response.status_code == 200

# Test GET nonexistent ID should return 404
def test_get_no_results(client):
    response = client.get("/lists/nonexistent-id")
    assert response.status_code == 404

# Test GET all list IDs
def test_get_all_lists(client):
    response = client.get("/lists")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# Test POST a duplicate list returns appropriate response
def test_post_duplicate(client):
    payload = {
        "destination": "tokyo",
        "duration": 4,
        "weather": "hot",
        "with_kids": False,
        "with_pet": True
    }
    first = client.post("/lists", json=payload)
    assert first.status_code == 201
    second = client.post("/lists", json=payload)
    assert second.status_code in [200, 409]

# Test PUT request updates an existing list
def test_put_update_existing(client):
    payload = {
        "destination": "london",
        "duration": 2,
        "weather": "rainy"
    }
    create = client.post("/lists", json=payload)
    list_id = create.get_json()["id"]

    update_payload = {
        "destination": "london",
        "duration": 5,
        "weather": "sunny"
    }
    update = client.put(f"/lists/{list_id}", json=update_payload)
    assert update.status_code == 200

    updated_item = get_dynamodb_item(list_id)
    updated_s3 = get_s3_object_content(list_id)
    assert updated_item["items"] == updated_s3["items"]

# Test PUT to nonexistent ID should return 404
def test_put_invalid_target(client):
    response = client.put("/lists/nonexistent", json={"duration": 10})
    assert response.status_code == 404

# Test DELETE an existing list
def test_delete_existing(client):
    payload = {
        "destination": "rome",
        "duration": 3
    }
    post = client.post("/lists", json=payload)
    list_id = post.get_json()["id"]

    delete = client.delete(f"/lists/{list_id}")
    assert delete.status_code == 200

    assert get_dynamodb_item(list_id) is None
    assert get_s3_object_content(list_id) is None

# Test DELETE nonexistent ID returns 404
def test_delete_invalid_target(client):
    response = client.delete("/lists/invalid-id")
    assert response.status_code == 404
