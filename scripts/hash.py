import os
import secrets

# Генерация случайного ключа
secret_key = secrets.token_hex(32)  # 32 байта = 64 символа в hex
print(secret_key)
