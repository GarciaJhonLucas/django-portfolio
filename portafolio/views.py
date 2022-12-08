from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos} )


def create(request):
    return render(request, 'create.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')