# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render

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