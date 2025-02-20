from frontend.models.vk_auth import make_vk_session
from dotenv import load_dotenv
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    flash,
    Response,
)
import sys
import os

load_dotenv()

VK_AUTH_URL = "https://oauth.vk.com/authorize"
VK_TOKEN_URL = "https://oauth.vk.com/access_token"
VK_CLIENT_SECRET = os.getenv("VK_APP_SECRET_KEY")

app_route = Blueprint("route", __name__)

@app_route.route("/")
@app_route.route("/index")
@app_route.route("/index.php")
@app_route.route("/index.htm")
@app_route.route("/index.html")
def index() -> str:
    """Функция отображения индексной страницы"""
    return render_template("index.html")

# Маршрут для начала аутентификации
@app_route.route("/login")
def login():
    vk = make_vk_session()
    auth_url, _ = vk.authorization_url(VK_AUTH_URL)
    return redirect(auth_url)

# Маршрут для обработки ответа от VK
@app_route.route("/callback")
def callback():
    try:
        vk = make_vk_session()
        token = vk.fetch_token(
            VK_TOKEN_URL,
            client_secret=VK_CLIENT_SECRET,
            authorization_response=request.url,
        )
        print(token)
        session["oauth_token"] = token
        return redirect(url_for("profile"))
    except Exception as e:
        return f"Error: {e}", 500

# Страница профиля пользователя
@app_route.route("/profile")
def profile():
    vk = make_vk_session(session.get("oauth_token"))
    user_info = vk.get("https://api.vk.com/method/users.get", params={"v": "5.131"}).json()
    return f"User info: {user_info}"
