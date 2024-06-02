# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from datetime import datetime

# @csrf_exempt
# def register_api(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'error': 'Username already exists.'}, status=400)
#         user = User.objects.create_user(username, password=password)
#         return JsonResponse({'message': 'User created successfully.'}, status=201)

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return JsonResponse({'error': 'Invalid username or password.'}, status=400)
#         login(request, user)
#         return JsonResponse({'message': 'Logged in successfully.'}, status=200)
    
def register(request):
    return render(request, 'bus/signup.html')

def login(request):
    return render(request, 'bus/signin.html')

def index(request):
    cities = City.objects.all()
    return render(request, 'bus/home.html', {'cities': cities})

def listings(request):
    if request.method == 'POST':
        from_city_name = request.POST['from_city']
        to_city_name = request.POST['to_city']
        date = datetime.strptime(request.POST['date'], "%Y-%m-%d").date()

        from_city = City.objects.get(name=from_city_name)
        to_city = City.objects.get(name=to_city_name)

        routes = Route.objects.filter(stops__city=from_city).filter(stops__city=to_city)

        trips = Trip.objects.filter(route__in=routes, time__date=date)

        return render(request, 'bus/listing.html', {'trips': trips})
    
def trip_details(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'bus/bus-details.html', {'trip': trip})


def create_trips(request):
    if request.method == 'POST':
        route_id = request.POST['route']
        vehicle_id = request.POST['vehicle']
        dates = request.POST.getlist('dates[]')

        route = Route.objects.get(pk=route_id)
        vehicle = TransportVehicle.objects.get(pk=vehicle_id)

        for date_str in dates:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            time = datetime.strptime('00:00:00', "%H:%M:%S").time()  # default time
            Trip.objects.create(route=route, transport_vehicle=vehicle, date=date, time=time)

        return redirect('index')

    routes = Route.objects.all()
    vehicles = TransportVehicle.objects.all()
    return render(request, 'bus/create_trips.html', {'routes': routes, 'vehicles': vehicles})