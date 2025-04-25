from flask import Flask
from .routes.example_route import get_example

def create_app():
    app = Flask(__name__)

    # Register routes
    app.add_url_rule('/example', view_func=get_example)
    
    @app.route('/')
    def home():
        return "Welcome to the Python Server App!"


    return app

if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)