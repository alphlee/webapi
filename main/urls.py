# capture/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.capture_view, name='capture'),
    path('result/', views.result_view, name='result'),
]
