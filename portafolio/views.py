from django.shortcuts import render, redirect
from .models import Proyecto, Visitante
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateForm, LoginForm, RegisterForm

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos} )


@login_required(login_url='login')
def dashboard(request):
    context={
        "proyectos": Proyecto.objects.all(),
        "cantidad": Proyecto.objects.count(),
        "visitantes": Visitante.objects.count(),
    }
    return render(request, 'dashboard.html', context )


@login_required(login_url='login')
def create(request):
    formulario = CreateForm
    
    if request.method == 'POST':
        create_form = CreateForm(request.POST)
        
        if create_form.is_valid():
            titulo = request.POST.get('titulo')
            descripcion = request.POST.get('descripcion')
            tags = request.POST.get('tags')
            imagen =  request.FILES['cimagen']
            url_github = request.POST.get('url_github')
            
            if Proyecto.objects.filter(url_github=url_github).exists():
                messages.warning(request, 'La URL del proyecto ya se registro')
                return redirect('create')
            else:
                proyecto = Proyecto(foto=imagen, titulo=titulo, descripcion=descripcion, tags=tags, url_github=url_github)
                proyecto.save()
                messages.success(request, 'El proyecto se creo correctamente')
                return redirect('dashboard')
        else:
            messages.warning(request, create_form.errors)
            return redirect('create')
    else:
        return render(request, 'create.html', {'forms':formulario})


@login_required(login_url='login')
def edit(request, **kwargs):
    formulario = CreateForm
    proyectos = Proyecto.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        try:
            edit_form = CreateForm(request.POST, instance=proyectos)
            edit_form.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'dashboard.html')
    else:
        formulario = CreateForm(instance=proyectos)
        return render(request, 'edit.html', {'forms':formulario})


@login_required(login_url='login')
def delete(request, **kwargs):
    proyectos = Proyecto.objects.get(id=kwargs['id'])
    proyectos.delete()
    return redirect('dashboard')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos} )


def login(request):
    formulario = LoginForm
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            username = request.POST.get('usuario')
            password = request.POST.get('contrasenia')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.success(request, 'Los datos son invalidos')
                return redirect('login')
        else:
            messages.warning(request, login_form.errors)
            return redirect('dashboard')
    else:
        return render(request, 'login.html', {'forms':formulario})
          

def register(request):
    formulario = RegisterForm
     
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            username = request.POST.get('usuario')
            email = request.POST.get('correo')
            password = request.POST.get('contrasenia')
            password2 = request.POST.get('rep_contrasenia')

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
            messages.warning(request, register_form.errors)
            return redirect('create')
    else:
        return render(request, 'register.html', {'forms':formulario})