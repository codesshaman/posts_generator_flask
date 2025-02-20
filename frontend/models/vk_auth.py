from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

VK_CLIENT_ID = os.getenv("VK_APP_ID")
VK_REDIRECT_URI = os.getenv("VK_REDIRECT_URL")


# Функция авторизации через VK
def make_vk_session(token=None):
    
    return OAuth2Session(
        client_id=VK_CLIENT_ID,
        redirect_uri=VK_REDIRECT_URI,
        token=token,
    )
