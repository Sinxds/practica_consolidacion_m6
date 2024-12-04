from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/agregar', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/listar_vehiculo', views.listar_vehiculo, name='listar_vehiculo'),
    path('posts/', views.posts, name='posts'),
]