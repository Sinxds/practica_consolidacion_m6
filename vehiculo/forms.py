from django.forms import ModelForm
from django import forms
from .models import Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'marca',
            'modelo',
            'serial_carroceria',
            'serial_motor',
            'categoria',
            'precio'
            ]