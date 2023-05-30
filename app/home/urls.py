from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('testing', views.testing, name='testing'),
    path('charts', views.charts, name='charts'),
]
