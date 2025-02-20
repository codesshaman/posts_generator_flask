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

app_route = Blueprint("route", __name__)

@app_route.route("/")
@app_route.route("/index")
@app_route.route("/index.php")
@app_route.route("/index.htm")
@app_route.route("/index.html")
def index() -> str:
    """Функция отображения индексной страницы"""
    return render_template("index.html")
