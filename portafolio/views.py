from django.shortcuts import render, redirect
from .models import Proyecto
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos} )

@login_required(login_url='login')
def create(request):
    return render(request, 'create.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['cusuario']
        password = request.POST['cpassword']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('create')
        else:
            messages.success(request, 'Los datos son invalidos')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['cusuario']
        email = request.POST['cmail']
        password = request.POST['cpassword']
        password2 = request.POST['cpasswords']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.success(request, 'El correo ya se registro')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.success (request, 'El usuario ya se registro')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.success (request, 'Las contraseñas no conciden')
            return redirect('register')
    else:
        return render(request, 'register.html')