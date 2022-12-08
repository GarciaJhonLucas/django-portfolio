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
    if request.method == 'POST':
        titulo = request.POST['ctitulo']
        descripcion = request.POST['cdescripcion']
        tags = request.POST['ctags']
        imagen = request.FILES.get('cimagen')
        url_pryecto = request.POST['curlproyecto']
        
        if Proyecto.objects.filter(url_github=url_pryecto).exists():
            messages.warning(request, 'La URL del proyecto ya se registro')
            return redirect('create')
        else:
            proyecto = Proyecto(foto=imagen, titulo=titulo, descripcion=descripcion, tags=tags, url_github=url_pryecto)
            proyecto.save()
            messages.success(request, 'El proyecto se creo correctamente')
            return redirect('create')
    else:
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