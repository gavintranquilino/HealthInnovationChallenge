from flask import Flask, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)
points = 0  # Stored integer variable

@app.route("/points", methods=["GET"])
def get_points():
    return jsonify({"points": points})

@app.route("/points", methods=["POST"])
def update_points():
    global points
    data = request.get_json()
    print(data)
    if "points" in data:
        points = data["points"]
        return jsonify({"message": "Points updated", "points": points})
    return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    # Start ngrok tunnel
    public_url = ngrok.connect(5000).public_url
    print(f"ngrok tunnel open at {public_url}")
    app.run(port=5000)
