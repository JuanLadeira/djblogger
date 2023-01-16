"""
BLOG URL Configuration
"""
from django.urls import path
from core.chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
