from django.contrib import admin
from django.urls import path
from Clinic_Ciper_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),
    path('', views.home_redirect, name='home_redirect'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),


    # Login
    path('login_paciente/', views.login_paciente, name='login_paciente'),
    path('login_medico/', views.login_medico, name='login_medico'),
    path('login_aux_administrativo/', views.login_aux_administrativo, name='login_aux_administrativo'),

    # Pacientes
    path('paciente/insertar/', views.insertar_paciente, name='insertar_paciente'),
    path('paciente/listar/', views.listar_paciente, name='listar_paciente'),
    path('paciente/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('paciente/inicio_paciente/', views.inicio_paciente, name='inicio_paciente'),
    path('paciente/actualizar/<int:id>/', views.actualizar_paciente, name='actualizar_paciente'),

    # Médicos
    path('medico/insertar/', views.insertar_medico, name='insertar_medico'),
    path('medico/eliminar/<int:id>/', views.eliminar_medico, name='eliminar_medico'),
    path('medico/listar/', views.listar_medico, name='listar_medico'),
    path('medico/inicio_medico/', views.inicio_medico, name='inicio_medico'),
    path('medico/actualizar/<int:id>/', views.actualizar_medico, name='actualizar_medico'),

    # Historia Clínica
    path('seleccionar_paciente/', views.seleccionar_paciente, name='seleccionar_paciente'),
    path('seleccionar_paciente_2/', views.seleccionar_paciente_2, name='seleccionar_paciente_2'),
    path('historia_clinica/insertar/<int:paciente_id>/', views.insertar_historia_clinica, name='insertar_historia_clinica'),
    path('historia_clinica/listar_historia_clinica/', views.listar_historia_clinica, name='listar_historia_clinica'),
    path('historia_clinica/listar_historia_clinica_2/<int:paciente_id>/', views.listar_historia_clinica_2, name='listar_historia_clinica_2'),
    path('historia_clinica/eliminar/<int:id>/', views.eliminar_historia_clinica, name='eliminar_historia_clinica'),

    # Auxiliares Administrativos
    path('auxiliar/insertar/', views.insertar_auxiliar, name='insertar_auxiliar'),
    path('auxiliar/listar/', views.listar_auxiliares, name='listar_auxiliares'),
    path('auxiliar/eliminar/<int:id>/', views.eliminar_auxiliar, name='eliminar_auxiliar'),
    path('inicio/', views.inicio_aux_administrativo, name='inicio_aux_administrativo'),
    path('auxiliar/actualizar/<int:id>/', views.actualizar_auxiliar, name='actualizar_auxiliar'),

    # Citas Médicas
    path('insertar/', views.insertar_cita, name='insertar_cita'),
    path('insertar', views.insertar_cita_2, name='insertar_cita_2'),
    path('listar/', views.listar_citas, name='listar_citas'),
    path('eliminar/<int:id>/', views.eliminar_cita, name='eliminar_cita'),

    # EPS
    path('eps/insertar/', views.insertar_eps, name='insertar_eps'),
    path('eps/listar/', views.listar_eps, name='listar_eps'),
    path('eps/eliminar/<int:id>/', views.eliminar_eps, name='eliminar_eps'),
    path('eps/actualizar/<int:id>/', views.actualizar_eps, name='actualizar_eps'),
]