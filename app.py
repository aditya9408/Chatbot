from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response  # Fixed typo in get_response import

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    
    # Check if the input is valid
    if not text or not isinstance(text, str):
        return jsonify({"error": "Invalid input"}), 400
    
    # Call the get_response function
    response = get_response(text)
    message = {"answer": response}
    
    # Return the response as a JSON object
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)