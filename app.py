from flask import Flask, redirect, request, session, url_for
from requests_oauthlib import OAuth2Session
from frontend.controllers.routes import app_route
from flask import Flask
import os

host = os.getenv('ALLOWED_HOST')
port = os.getenv('ALLOWED_PORT')
secret_key = os.getenv('SECRET_KEY')

# Настройки VK OAuth
VK_CLIENT_ID = os.getenv("VK_APP_ID")
VK_CLIENT_SECRET = os.getenv("VK_APP_SECRET_KEY")
VK_REDIRECT_URI = os.getenv("VK_REDIRECT_URL")  # Должен совпадать с настройками VK
VK_AUTH_URL = "https://oauth.vk.com/authorize"
VK_TOKEN_URL = "https://oauth.vk.com/access_token"

# Создаём Flask-приложение
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Настройка сессии
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Функция авторизации через VK
def make_vk_session(token=None):
    return OAuth2Session(
        client_id=VK_CLIENT_ID,
        redirect_uri=VK_REDIRECT_URI,
        token=token,
    )

# Маршрут для начала аутентификации
@app.route("/login")
def login():
    vk = make_vk_session()
    auth_url, _ = vk.authorization_url(VK_AUTH_URL)
    return redirect(auth_url)

# Маршрут для обработки ответа от VK
@app.route("/callback")
def callback():
    vk = make_vk_session()
    token = vk.fetch_token(
        VK_TOKEN_URL,
        client_secret=VK_CLIENT_SECRET,
        authorization_response=request.url,
    )
    session["oauth_token"] = token
    return redirect(url_for("profile"))

# Страница профиля пользователя
@app.route("/profile")
def profile():
    vk = make_vk_session(session.get("oauth_token"))
    user_info = vk.get("https://api.vk.com/method/users.get", params={"v": "5.131"}).json()
    return f"User info: {user_info}"

app.register_blueprint(app_route)

if __name__ == "__main__":
    app.run(host, port)
