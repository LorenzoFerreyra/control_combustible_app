from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Empleado, Equipo, Ruta, Actividad, EnTransito
from .forms import EmpleadoForm, EquipoForm, RutaForm, ActividadForm, EnTransitoForm

@login_required
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

@login_required
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
            messages.success(request, 'Empleado creado exitosamente.')
            return redirect('crear_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'crear_empleado.html', {'form': form})

def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_personal')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        messages.error(request, 'Empleado eliminado exitosamente.')
        return redirect('lista_personal')
    return redirect('lista_personal')

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo creado exitosamente.')
            return redirect('crear_equipo')
    else:
        form = EquipoForm()
    return render(request, 'crear_equipo.html', {'form': form})

def editar_equipo(request, id_item):
    equipo = get_object_or_404(Equipo, id_item=id_item)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipo')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'editar_equipo.html', {'form': form, 'equipo': equipo})

def eliminar_equipo(request, id_item):
    equipo = get_object_or_404(Equipo, id_item=id_item)
    if request.method == 'POST':
        equipo.delete()
        messages.error(request, 'Equipo eliminado exitosamente.')
        return redirect('lista_equipo')
    return redirect('lista_equipo')

def ruta_list(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta_list.html', {'rutas': rutas})

def crear_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta creada exitosamente.')
            return redirect('crear_ruta')
    else:
        form = RutaForm()
    return render(request, 'crear_ruta.html', {'form': form})

def editar_ruta(request, ruta):
    ruta = get_object_or_404(Ruta, ruta=ruta)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            return redirect('lista_ruta')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'editar_ruta.html', {'form': form, 'ruta': ruta})

def eliminar_ruta(request, ruta):
    ruta = get_object_or_404(Ruta, ruta=ruta)
    if request.method == 'POST':
        ruta.delete()
        messages.error(request, 'Ruta eliminada exitosamente.')
        return redirect('lista_ruta')
    return redirect('lista_ruta')

def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividad_list.html', {'actividades': actividades})

def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actividad creada exitosamente.')
            return redirect('lista_actividad')
    else:
        form = ActividadForm()
    return render(request, 'crear_actividad.html', {'form': form})

def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('lista_actividad')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html', {'form': form, 'actividad': actividad})

def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        actividad.delete()
        messages.error(request, 'Actividad eliminada exitosamente.')
        return redirect('lista_actividad')
    return redirect('lista_actividad')

def informes(request):
    return render(request, 'informes.html')


def crear_en_transito(request):
    if request.method == 'POST':
        form = EnTransitoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro en tránsito creado exitosamente.')
            return redirect('informes')
    else:
        form = EnTransitoForm()
    
    return render(request, 'crear_entransito.html', {'form': form})

def registros_entransito(request):
    entransitos = EnTransito.objects.all()
    return render(request, 'entransito_registros.html', {'entransitos': entransitos})

def editar_entransito(request, numero):
    entransito = get_object_or_404(EnTransitoForm, numero=numero)
    if request.method == 'POST':
        form = EnTransitoForm(request.POST, instance=entransito)
        if form.is_valid():
            form.save()
            return redirect('informes')
    else:
        form = EnTransitoForm(instance=entransito)
    return render(request, 'editar_entransito.html', {'form': form, 'entransito': entransito})