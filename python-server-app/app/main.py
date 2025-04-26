from flask import Flask, request
from .routes.example_route import get_example
import requests

app = Flask(__name__)

# Register routes
app.add_url_rule('/example', view_func=get_example)

@app.route('/')
def home():
    return "Welcome to the Python Server App!"

@app.route('/suggest_movie', methods=['POST'])
def suggest_movie():
    data = request.get_json()
    if not data or 'text' not in data:
        return {"error": "Invalid input, 'text' field is required"}, 400
    text = data['text']

    try:
        response = requests.post('https://agent-suggester-service-url/suggest', json={"text": text})
        response.raise_for_status()
        return response.json()  # Assuming the service returns JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

@app.route('/suggest_dummy', methods=['GET'])
def suggest_dummy():
    try:
        response = request.get('https://agent-suggester-service-url/example')
        response.raise_for_status()
        return response.json()  # Assuming the service returns JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)