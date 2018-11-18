"""Making URL pattern for blog mapping app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]