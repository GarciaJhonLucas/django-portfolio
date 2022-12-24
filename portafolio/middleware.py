from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip
from .models import Visitante

def ip_register(get_response):
    def middleware(request):
        ip,is_routable=get_client_ip(request)
        ipBd=Visitante.objects.filter(ip=ip).first()
        if ipBd is None:
            ipBd=Visitante(ip=ip)
            ipBd.save()
        response = get_response(request)
        return response
    return middleware