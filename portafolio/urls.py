from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portafolio'),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
