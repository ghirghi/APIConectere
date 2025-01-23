from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your API endpoint
API_URL = "https://api.example.com/data"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetch-data", methods=["GET"])
def fetch_data():
    response = requests.get(API_URL)
    data = response.json()
    return jsonify(data)

@app.route("/manipulate-data", methods=["POST"])
def manipulate_data():
    data = request.json
    # Add your manipulation logic
    manipulated_data = {"manipulated": True, **data}
    return jsonify(manipulated_data)

if __name__ == "__main__":
    app.run(debug=True)
