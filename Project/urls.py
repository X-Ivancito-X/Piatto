"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 2.1 Importamos include para llamar a otro arhcivo fuera de este
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 2.2 Incluimos el archivo "urls" que viene de "App"
    # 3er PASO crear archivo "urls" en "App" para crear nuestras url
    path('', include ('App.urls')),

]
