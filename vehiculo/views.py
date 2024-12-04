from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VehiculoForm
from .models import Vehiculo
from . import views
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def agregar_vehiculo(request):
    contexto = {}
    contexto["form"] = VehiculoForm()
       
    if request.method == 'GET':
        return render(request, 'vehiculo/agregar_vehiculo.html', contexto)
   
    if request.method == 'POST':
       
        form = VehiculoForm(request.POST)
        contexto["form"] = form
       
        if form.is_valid():
            print(form)
            form.save()
           
            messages.success(request, "Se ha añadido el automóvil exitosamente.")
            return redirect('posts')
           
        else:
            messages.error(request, "Error. Revise los datos ingresados.")
            return render(request, 'vehiculo/agregar_vehiculo.html', contexto)
        
        
def posts(request):
    return render(request, 'posts.html')


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()

    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.rango_precio = "Bajo"
        elif vehiculo.precio <= 30000:
            vehiculo.rango_precio = "Medio"
        else:
            vehiculo.rango_precio = "Alto"

    context = {
        'vehiculos': vehiculos,
    }
    return render(request, 'vehiculo/listar_vehiculo.html', context)

""" def listar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculo.html', {'vehiculos': vehiculos}) """