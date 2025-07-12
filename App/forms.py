# llamamos a la libreria asignada de django forms
from django import forms
# llamamos a nuestro model para traer la tabla
from .models import *

# Formulario para generar el entorno
class VerForm(forms.ModelForm):
    class Ver:
        # model treae la base  de daots
        model=Productos
        # fields trae los atributos
        fields='__all__'

class FormRegistrar(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields='__all__'