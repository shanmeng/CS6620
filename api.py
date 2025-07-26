
# Name: Shan Meng
# Date: July 25, 2025
# Class: CS6620
# Notes: Assignment CI/CD pipeline part 3

from flask import Flask, request, jsonify
from PackMyBag import suggest_items
import boto3
import json
import os
from botocore.exceptions import ClientError

app = Flask(__name__)

# AWS LocalStack configurations
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1",
    endpoint_url=os.getenv("DYNAMODB_ENDPOINT", "http://localstack:4567")
)
s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    endpoint_url=os.getenv("S3_ENDPOINT", "http://localstack:4567")
)

TABLE_NAME = "PackingLists"
BUCKET_NAME = "packing-lists-bucket"

# Ensure resources exist
def ensure_resources():
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
        )
    except ClientError as e:
        if "ResourceInUseException" not in str(e):
            raise

    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
    except ClientError as e:
        if "BucketAlreadyOwnedByYou" not in str(e):
            raise

ensure_resources()
table = dynamodb.Table(TABLE_NAME)

# POST method
@app.route("/lists", methods=["POST"])
def create_list():
    try:
        data = request.get_json()
        destination = data.get("destination")
        duration = int(data.get("duration", 1))
        weather = data.get("weather", "mild")
        with_kids = data.get("with_kids", False)
        with_pet = data.get("with_pet", False)
        list_id = data.get("id", f"{destination}_{duration}")

        if not destination:
            return {"error": "Missing 'destination'"}, 400

        packing_list = suggest_items(destination, duration, weather, with_kids, with_pet)

        # Save to DynamoDB
        table.put_item(Item={
            "id": list_id,
            "destination": destination,
            "duration": duration,
            "weather": weather,
            "with_kids": with_kids,
            "with_pet": with_pet
        })

        # Save to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=f"{list_id}.json",
            Body=json.dumps(packing_list)
        )

        return jsonify({"id": list_id, "items": packing_list}), 201

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

# GET method
@app.route("/lists/<list_id>", methods=["GET"])
def get_list(list_id):
    try:
        item = table.get_item(Key={"id": list_id}).get("Item")
        if not item:
            return {"error": "List not found"}, 404

        s3_obj = s3.get_object(Bucket=BUCKET_NAME, Key=f"{list_id}.json")
        packing_list = json.loads(s3_obj["Body"].read())

        return jsonify({"id": list_id, "details": item, "items": packing_list}), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve list", "details": str(e)}), 500

# PUT method
@app.route("/lists/<list_id>", methods=["PUT"])
def update_list(list_id):
    try:
        data = request.get_json()
        update_fields = {k: v for k, v in data.items() if k != "id"}

        # Update DynamoDB
        update_expr = "SET " + ", ".join(f"{k}=:{k}" for k in update_fields)
        expr_values = {f":{k}": v for k, v in update_fields.items()}

        table.update_item(
            Key={"id": list_id},
            UpdateExpression=update_expr,
            ExpressionAttributeValues=expr_values
        )

        # Optionally update S3
        if "items" in data:
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=f"{list_id}.json",
                Body=json.dumps(data["items"])
            )

        return {"message": f"List {list_id} updated successfully"}, 200
    except Exception as e:
        return jsonify({"error": "Failed to update list", "details": str(e)}), 500

# DELETE method
@app.route("/lists/<list_id>", methods=["DELETE"])
def delete_list(list_id):
    try:
        table.delete_item(Key={"id": list_id})
        s3.delete_object(Bucket=BUCKET_NAME, Key=f"{list_id}.json")
        return {"message": f"List {list_id} deleted successfully"}, 200
    except Exception as e:
        return jsonify({"error": "Failed to delete list", "details": str(e)}), 500

# GET all IDs
@app.route("/lists", methods=["GET"])
def list_all_ids():
    try:
        scan = table.scan(AttributesToGet=["id"])
        ids = [item["id"] for item in scan.get("Items", [])]
        return jsonify({"all_ids": ids}), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch IDs", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
