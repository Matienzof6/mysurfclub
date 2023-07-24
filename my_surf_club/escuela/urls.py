from django.urls import path

from . import views

urlpatterns = [
    path('escuela/', views.escuela, name='escuela'),
]