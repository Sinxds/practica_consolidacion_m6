from django.urls import path
from .views import UsuarioRegistroView
from .views import UsuarioLoginView
from .views import UsuarioLogoutView
from . import views

urlpatterns = [
    path('registro/', UsuarioRegistroView.as_view(), name='registro'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.UsuarioLogoutView.as_view(), name='logout'),
    path('perfil/<int:user_id>/', views.Perfil, name='perfil'),
]
