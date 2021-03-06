from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import formulario_atend
from .models import atender, publico, tipo


def home(request):
    atendimentos = atender.objects.all().order_by('-atendimento')
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
    total_atend = atender.objects.all().aggregate(
        Total_atendimentos=Count('atendimento'))

    porp = publico.objects.values(
        'publico').annotate(qtd=Count('atendidos__publico'))

    portipo = tipo.objects.values(
        'tipo').annotate(qtd2=Count('atendidos__tipo'))

    return render(request, 'dashboard.html',
                  {'total_atend': total_atend,
                   'contagem': porp,
                   'contportipo': portipo,
                   })
