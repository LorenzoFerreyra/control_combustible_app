from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('personal_list/', views.personal_list, name='lista_personal'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('editar_empleado/<uuid:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<uuid:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('equipo_list/', views.equipo_list, name='lista_equipo'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('editar_equipo/<uuid:id_item>/', views.editar_equipo, name='editar_equipo'),
    path('eliminar_equipo/<uuid:id_item>/', views.eliminar_equipo, name='eliminar_equipo'),
]
