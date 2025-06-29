
# Name: Shan Meng
# Date: June 25, 2025
# Class: CS6620
# Notes: Assignment CI/CD pipeline part 2, updated on June 28 based on professor's feedback



import pytest
from api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Testing POST
def test_create_list_with_id(client):
    response = client.post("/lists", json={
        "id": "trip_create",
        "destination": "Rome",
        "duration": 3,
        "weather": "hot",
        "with_kids": False,
        "with_pet": True
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["id"] == "trip_create"
    assert "items" in data


# Testing POST and GET
def test_get_list_by_id(client):
    client.post("/lists", json={
        "id": "trip_get",
        "destination": "London",
        "duration": 2
    })
    response = client.get("/lists/trip_get")
    assert response.status_code == 200
    assert response.get_json()["id"] == "trip_get"


# Testing POST and PUT
def test_update_existing_list(client):
    client.post("/lists", json={
        "id": "trip_update",
        "destination": "Berlin",
        "duration": 4
    })
    response = client.put("/lists/trip_update", json={
        "extras": ["camera", "travel adapter"]
    })
    assert response.status_code == 200
    assert "updated" in response.get_json()["message"]


# Testing POST and DELETE
def test_delete_existing_list(client):
    client.post("/lists", json={
        "id": "trip_delete",
        "destination": "Tokyo",
        "duration": 5
    })
    response = client.delete("/lists/trip_delete")
    assert response.status_code == 200
    assert "deleted" in response.get_json()["message"]


def test_list_all_ids(client):
    # Make sure to start clean
    client.post("/lists", json={"id": "trip_a", "destination": "NYC", "duration": 1})
    client.post("/lists", json={"id": "trip_b", "destination": "SF", "duration": 2})
    response = client.get("/lists")
    assert response.status_code == 200
    ids = response.get_json()["all_ids"]
    assert "trip_a" in ids
    assert "trip_b" in ids


# Testing POST with missing required field
def test_create_list_missing_destination(client):
    response = client.post("/lists", json={
        "id": "missing_destination",
        "duration": 2
    })
    assert response.status_code == 400
    assert "destination" in response.get_json()["error"]


# Testing GET non-existent ID
def test_get_nonexistent_list(client):
    response = client.get("/lists/nonexistent_id")
    assert response.status_code == 404
    assert "not found" in response.get_json()["error"]


# Testing PUT non-existent ID
def test_update_nonexistent_list(client):
    response = client.put("/lists/ghost_trip", json={"extra": "sunglasses"})
    assert response.status_code == 404
    assert "not found" in response.get_json()["error"]


# Testing DELETE non-existent ID
def test_delete_nonexistent_lists(client):
    response = client.delete("/lists/ghost_trip")
    assert response.status_code == 404
    assert "not found" in response.get_json()["error"]


# Simulate server error: POST with invalid JSON
def test_post_invalid_json(client):
    response = client.post("/lists", data="not_a_json", content_type="application/json")
    assert response.status_code == 500
    assert "Internal Server Error" in response.get_json()["error"]
    
