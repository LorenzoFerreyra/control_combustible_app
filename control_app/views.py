from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.models import User, Empleado
from django.contrib.auth.decorators import login_required
from .models import Empleado, Equipo, Ruta, Actividad

#@login_required
def index(request):
    return render(request, 'index.html')

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("Ha iniciado sesión."))
			return redirect('index')
		else:
			messages.success(request, ("Error. Inténtelo otra vez."))
			return redirect('login')

	else:
		return render(request, 'login.html', {})

#@login_required
def logout_user(request):
	logout(request)
	messages.success(request, ("Cerró sesión. Gracias por visitarnos."))
	return redirect('index')

def personal_list(request):
    personal = Empleado.objects.all()
    return render(request, 'personal_list.html', {'personal': personal})

def equipo_list(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo_list.html', {'equipos': equipos})

def ruta_list(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta_list.html', {'rutas': rutas})

def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividad_list.html', {'actividades': actividades})