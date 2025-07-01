
# Name: Shan Meng
# Date: June 25, 2025
# Class: CS6620
# Notes: Assignment CI/CD pipeline part 2, updated on Jun 28 based on professor's feedback



from flask import Flask, request, jsonify
from PackMyBag import suggest_items

app = Flask(__name__)

# Store generated lists
saved_lists = {}


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
    
        # Generate ID automatically if not provided
        list_id = data.get("id", f"{destination}_{duration}")
    
        if not destination:
            return {"error": "Missing 'destination'"}, 400
    
        packing_list = suggest_items(destination, duration, weather, with_kids, with_pet)
        saved_lists[list_id] = packing_list
    
        return jsonify({"id": list_id, "items": packing_list}), 201
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

# GET method
@app.route("/lists/<list_id>", methods=["GET"])
def get_list(list_id):
    try:
        if list_id not in saved_lists:
            return {"error": "List not found"}, 404
        return jsonify({"id": list_id, "items": saved_lists[list_id]}), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

# PUT method
@app.route("/lists/<list_id>", methods=["PUT"])
def update_list(list_id):
    try:
        if list_id not in saved_lists:
            return {"error": "List not found"}, 404
        updates = request.get_json()
        saved_lists[list_id].update(updates)
        return {"message": f"List '{list_id}' updated."}, 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

# DELETE method
@app.route("/lists/<list_id>", methods=["DELETE"])
def delete_list(list_id):
    try:
        if list_id not in saved_lists:
            return {"error": "List not found"}, 404
        del saved_lists[list_id]
        return {"message": f"List '{list_id}' deleted."}, 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

# GET method
@app.route("/lists", methods=["GET"])
def list_all():
    try:
        return jsonify({"all_ids": list(saved_lists.keys())}), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

