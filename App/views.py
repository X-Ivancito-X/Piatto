# Metodo redirect para redireccionar
from django.shortcuts import render, redirect, get_object_or_404
# Incorporamos el metodo de loguot para deslogearse
from django.contrib.auth import logout
from .models import *
from .forms import *

# Funcion + Nombre de la funcion + Parametro
def Inicio(request):
    # retornamos 
    return render(request,"Index.html")
def Nosotros(request):
    # retornamos 
    return render (request, 'Page/Nosotros.html')
def VerMas(request):
    # retornamos 
    return render (request, 'Page/VerMas.html')

def Registrar(request):
    data={
        'formRegistrar':FormRegistrar()
    }
    if request.method=='POST':
        query=FormRegistrar(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['formRegistrar']=FormRegistrar
    # retornamos 
    return render (request, 'Page/CrearCuenta.html', data)

# Funcion para deslogearse
def Salir(request):
    logout(request)
# ---------------------¬Este nombre "Index" proviene del archivo "urls.py"
    return redirect('Index')

# Mostramos porductos de models
def VerProductos(request):
    Mostrar=Productos.objects.all().order_by()('IdProducto')[:10]
    data={
        'VerProdouctos':Mostrar

    }
    return render (request, "Pages/VerMas.html", data)

# MODIFICAR PRODUCTO 
def Modificar(request, Cod):
    # ---------------------->TABLA--->ID (BD)=Parametro
    query=get_object_or_404(Productos, IdProducto=Cod)
    data={
        'forms':VerForm(instance=query)
    }
    if request.method=='POST':
        query=VerForm(data=request.POST,instance=query,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:

            data['forms']=VerForm
    return render(request,'Administrador.html',data)


