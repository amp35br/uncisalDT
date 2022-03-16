from django.urls import path

from atendimento.views import home

urlpatterns = [
    path('', home),
]
