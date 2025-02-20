from flask import Flask, redirect, request, session, url_for
from frontend.controllers.routes import app_route
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
import os

# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

load_dotenv()

host = os.getenv('ALLOWED_HOST')
port = os.getenv('ALLOWED_PORT')
cert = os.getenv('SSL_CERT')
key  = os.getenv('SSL_KEY')
# secret_key = os.getenv('SECRET_KEY')


# Создаём Flask-приложение
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")
# Настройка сессии
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


app.register_blueprint(app_route)

if __name__ == "__main__":
    app.run(
        host=host,
        port=port,
        ssl_context=(cert, key)
    )
