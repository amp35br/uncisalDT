from django.shortcuts import render

from .models import atender


def home(request):
    atendimentos = atender.objects.all()
    return render(request, 'home.html', {'atendimentos': atendimentos})
