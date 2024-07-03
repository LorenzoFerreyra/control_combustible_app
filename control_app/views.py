from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.models import User, Empleado
from django.contrib.auth.decorators import login_required

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

