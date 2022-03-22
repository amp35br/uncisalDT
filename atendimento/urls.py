from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('detalhe/<int:id>', views.detalhe, name='detalhe_view'),
    path('formatend/', views.formatend, name='formatend_view'),
    path('formedit/<int:atender_pk>', views.formedit, name='formedit_view'),
    path('formdelete/<int:atender_pk>', views.formdelete, name='fdel_view'),
    path('dashboard/', views.dashboard, name='dashboard_view'),
]
