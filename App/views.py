from django.shortcuts import render

# Funcion + Nombre de la funcion + Parametro
def Inicio(request):
    # retornamos 
    return render(request,"Index.html")

