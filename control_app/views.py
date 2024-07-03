from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.models import User, Empleado
from django.contrib.auth.decorators import login_required
from .models import Empleado, Equipo, Ruta, Actividad
from .forms import EmpleadoForm

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

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'crear_empleado.html', {'form': form})

def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'eliminar_empleado.html', {'empleado': empleado})