"""
BLOG URL Configuration
"""
from django.urls import path
from core.blog.views import HomePageView, singlepostview

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('<slug:post>/', singlepostview, name='post_single')

]
