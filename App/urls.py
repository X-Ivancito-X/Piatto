# Incluimos path
from django.urls import path
# Importamos la HOJA DE VISTAS
# ".views" xq es un archivo interno + "*" traemos todo
from .views import *

urlpatterns = [
    # Ruta + Nombre de la funcion que viene de .views + html
    path('',Inicio,name="Index"),

]
# 4to PASO creamos las funciones en ".views"
# para llamarlas aca y se ejecuten