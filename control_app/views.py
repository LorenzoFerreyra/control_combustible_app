from django.shortcuts import render

def index(request):
    return render(request, 'control_app/index.html')
