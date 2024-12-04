from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.models import Permission

from django.contrib.auth.models import User
from .models import Perfil

class UsuarioRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)

        usuario = form.instance
        permiso = Permission.objects.get(codename='visualizar_catalogo')
        usuario.user_permissions.add(permiso)
        usuario.save()

        messages.success(self.request, 'Registro éxitoso.')
        return response
    
    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículo")
        ]


class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    
    def form_valid(self, form):
        
        messages.success(self.request, 'Sesión iniciada con éxito.')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
    
class UsuarioLogoutView(LogoutView):
    next_page = 'index'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Has cerrado la sesión.')
        return super().dispatch(request, *args, **kwargs)