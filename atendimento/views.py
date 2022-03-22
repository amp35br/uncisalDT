from django.shortcuts import get_object_or_404, redirect, render

from .forms import formulario_atend
from .models import atender


def home(request):
    atendimentos = atender.objects.all()
    return render(request, 'home.html', {'atendimentos': atendimentos})


def detalhe(request, id):
    detalhe = get_object_or_404(atender, pk=id)
    return render(request, 'detalhe.html', {'detalhe': detalhe})


def formatend(request):
    form = formulario_atend(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home_view')

    return render(request, 'formatend.html', {'form': form})


def formedit(request, atender_pk):
    edicao = atender.objects.get(pk=atender_pk)

    form = formulario_atend(request.POST or None, instance=edicao)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home_view')

    return render(request, 'formedit.html', {'form': form})


def formdelete(request, atender_pk):
    formdel = atender.objects.get(pk=atender_pk)
    formdel.delete()

    return redirect('home_view')


def dashboard(request):

    return render(request, 'dashboard.html')
