from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('personal_list/', views.personal_list, name='lista_personal'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('editar_empleado/<uuid:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<uuid:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
]
