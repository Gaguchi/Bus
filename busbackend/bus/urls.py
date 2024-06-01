# bus/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('register_api/', views.register_api, name='register_api'),
    # path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('listings/', views.listings, name='listings'),
    path('', views.index, name='index'),
    path('bus-details/<int:trip_id>/', views.trip_details, name='bus-details'),
    path('create-trips/', views.create_trips, name='create-trips'),
]