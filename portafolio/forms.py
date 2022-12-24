from django import forms
from .models import Proyecto

class CreateForm(forms.ModelForm):
    titulo = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control-input',
        'id':'ctitulo'
    }))
    descripcion = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
        'class':'form-control-input',
        'id':'cdescripcion'
    }))
    tags = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
        'class':'form-control-input',
        'id':'ctags'
    }))

    url_github = forms.CharField(
        required=True, widget=forms.URLInput(attrs={
        'class':'form-control-input',
        'id':'curlproyecto',
    }))
    class Meta:
        model = Proyecto
        fields = ['titulo','descripcion','tags','url_github']
    
    
class LoginForm(forms.Form):
    usuario = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control-input',
        'id':'cusuario'
    }))
    contrasenia = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control-input',
        'id':'cpassword'
    }))
    

class RegisterForm(forms.Form):
    usuario = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control-input',
        'id':'cusuario'
    }))
    correo = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={
        'class':'form-control-input',
        'id':'cmail'
    }))
    contrasenia = forms.CharField(
        required=True, min_length=8, widget=forms.PasswordInput(attrs={
        'class':'form-control-input',
        'id':'cpassword'
    }))
    rep_contrasenia = forms.CharField(
        required=True, min_length=8, widget=forms.PasswordInput(attrs={
        'class':'form-control-input',
        'id':'cpasswords'
    }))
    