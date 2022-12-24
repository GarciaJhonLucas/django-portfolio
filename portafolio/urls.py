from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portafolio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
