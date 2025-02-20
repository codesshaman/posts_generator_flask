from flask import Flask, redirect, url_for, session
from flask_dance import OAuth2ConsumerBlueprint
from flask_dance.contrib.vk import make_vk_blueprint, vk

# Создайте приложение Flask
app = Flask(__name__)
app.secret_key = "some_secret"
app.config["SESSION_COOKIE_NAME"] = "vk_oauth_session"

# Настройка OAuth с ВКонтакте
vk_bp = make_vk_blueprint(client_id="YOUR_VK_APP_ID", client_secret="YOUR_VK_APP_SECRET", redirect_to="vk_login")
app.register_blueprint(vk_bp, url_prefix="/vk_login")

@app.route('/')
def index():
    if not vk.authorized:
        return redirect(url_for('vk.login'))
    resp = vk.get('users.get')
    assert resp.ok, resp.text
    user_info = resp.json()[0]
    return f'Привет, {user_info["first_name"]} {user_info["last_name"]}!'

@app.route('/logout')
def logout():
    # Завершаем сессию и выводим на главную страницу
    session.pop('vk_oauth_token', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
