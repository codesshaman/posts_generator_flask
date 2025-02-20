from flask import Flask, redirect, request, session, url_for
from frontend.controllers.routes import app_route
from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

host = os.getenv('ALLOWED_HOST')
port = os.getenv('ALLOWED_PORT')
# secret_key = os.getenv('SECRET_KEY')


# Создаём Flask-приложение
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Настройка сессии
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


app.register_blueprint(app_route)

if __name__ == "__main__":
    app.run(host='192.168.1.135', port='1024')
