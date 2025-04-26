from flask import Flask
from llm_agent.planner import handle_request, anthropic_test
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Suggester App!"

@app.route('/example', methods=['GET'])
def example_route():
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