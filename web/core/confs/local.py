from core.confs.settings import *
from decouple import config

ALLOWED_HOSTS.append("*")


DB_USERNAME = config("POSTGRES_USER")
DB_NAME = config("POSTGRES_DB")
DB_PASSWORD = config("POSTGRES_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("POSTGRES_PORT")

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
