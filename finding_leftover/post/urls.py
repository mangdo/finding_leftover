from django.contrib import admin
from django.urls import path, include
from post import views

urlpatterns = [
    path('', views.PostList.as_view())
]