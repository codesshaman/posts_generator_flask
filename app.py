from frontend.controllers.routes import app_route
from flask import Flask
import os

host = os.getenv('ALLOWED_HOST')
port = os.getenv('ALLOWED_PORT')
secret_key = os.getenv('SECRET_KEY')

def create_app():
    my_app = Flask(__name__)
    app.secret_key = secret_key
    app.config["SESSION_COOKIE_NAME"] = "vk_oauth_session"
    return my_app

app = create_app()

app.register_blueprint(app_route)

if __name__ == "__main__":
    app.run(host, port)
