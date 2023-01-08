"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if os.environ.get("DEBUG") == "1":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.confs.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.confs.production")

application = get_asgi_application()
