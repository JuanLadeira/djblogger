from decouple import config

from .settings import *

ALLOWED_HOST = config("ENV_ALLOWED_HOSTS")
if ALLOWED_HOST:
    ALLOWED_HOSTS = [ALLOWED_HOST]


DB_USERNAME = config("POSTGRES_USER_PD")
DB_NAME = config("POSTGRES_DB_PD")
DB_PASSWORD = config("POSTGRES_PASSWORD_PD")
DB_HOST = config("POSTGRES_HOST_PD")
DB_PORT = config("POSTGRES_PORT_PD")

DB_IS_AVAILABLE = all([DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT])

DB_IGNORE_SSL = config("DB_IGNORE_SSL") == "true"
POSTGRES_READY = 1

if DB_IS_AVAILABLE and POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_NAME,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "PORT": DB_PORT,
            "HOST": DB_HOST,
        }
    }
    if not DB_IGNORE_SSL:
        DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}
