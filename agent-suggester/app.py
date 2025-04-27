from flask import Flask
from llm_agent.planner import handle_request, anthropic_test
from flask import request
import logging
import google.cloud.logging

def init_logging():
    # Initialize the Cloud Logging client
    logging_client = google.cloud.logging.Client()

    # Set up the Cloud Logging handler
    logging_client.setup_logging()

    # Now you can use the standard logging module
    logging.info("This is an informational message.")
    logging.error("This is an error message.")

init_logging()

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Suggester App!"

@app.route('/example', methods=['GET'])
def example_route():
    logging.info("Received request for example route")
    return anthropic_test()

@app.route('/suggest', methods=['POST'])
def process_text_body():
    data = request.get_json()
    if not data or 'text' not in data:
        return {"error": "Invalid input, 'text' field is required"}, 400
    text = data['text']
    return handle_request(text)


if __name__ == '__main__':
    app.run(debug=True)