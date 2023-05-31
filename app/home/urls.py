from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('testing', views.testing, name='testing'),
    path('courses', views.courses, name='courses')
]
