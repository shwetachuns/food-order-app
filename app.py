from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Define the URL of the food order API
API_URL = "https://api.example.com/food_order_details"

@app.route("/")
def index():
    # Fetch data from the API
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return render_template("index.html", data=data)
    else:
        return render_template("error.html", message="Failed to fetch data from the API")

if __name__ == "__main__":
    app.run(debug=False)
