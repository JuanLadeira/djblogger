"""
BLOG URL Configuration
"""
from core.blog.views import (HomePageView, PostSearchView, TagListView,
                             singlepostview)
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('search/', PostSearchView.as_view() , name="post_search"),
    path('<slug:post>/', singlepostview, name='post_single'),
    path('tag/<slug:tag>/', TagListView.as_view(), name="post_by_tag"),
]
