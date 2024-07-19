from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('personal_list/', views.personal_list, name='lista_personal'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('editar_empleado/<uuid:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<uuid:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('equipo_list/', views.equipo_list, name='lista_equipo'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('editar_equipo/<uuid:id_item>/', views.editar_equipo, name='editar_equipo'),
    path('eliminar_equipo/<uuid:id_item>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('ruta_list/', views.ruta_list, name='lista_ruta'),
    path('crear_ruta/', views.crear_ruta, name='crear_ruta'),
    path('editar_ruta/<ruta>/', views.editar_ruta, name='editar_ruta'),
    path('eliminar_ruta/<ruta>/', views.eliminar_ruta, name='eliminar_ruta'),
    path('actividad_list/', views.actividad_list, name='lista_actividad'),
    path('crear_actividad/', views.crear_actividad, name='crear_actividad'),
    path('editar_actividad/<id>/', views.editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<id>/', views.eliminar_actividad, name='eliminar_actividad'),
    path('informes/', views.informes, name='informes'),
    path('crear_entransito/', views.crear_en_transito, name='crear_en_transito'),
]
