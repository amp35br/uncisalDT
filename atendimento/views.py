from django.shortcuts import get_object_or_404, render

from .models import atender


def home(request):
    atendimentos = atender.objects.all()
    return render(request, 'home.html', {'atendimentos': atendimentos})


def detalhe(request, id):
    detalhe = get_object_or_404(atender, pk=id)
    return render(request, 'detalhe.html', {'detalhe': detalhe})
