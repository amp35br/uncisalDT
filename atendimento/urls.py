from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('detalhe/<int:id>', views.detalhe, name='detalhe_view')
]
