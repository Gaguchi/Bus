# bus/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('register_api/', views.register_api, name='register_api'),
    # path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]