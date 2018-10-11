# accounts/urls.py
from django.urls import path

from usuario import views


urlpatterns = [
    path('registro-medico/', views.RegistroMedico, name='registro-medico'),
    path('registro-paciente/', views.RegistroPaciente, name='registro-paciente'),
    path('login/', views.login_user, name='login'),
]