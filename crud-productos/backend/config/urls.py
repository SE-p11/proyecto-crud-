"""
URL configuration for config project.

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
from django.urls import path, include

# Lista principal donde se registran todas las rutas (URLs) globales del proyecto
urlpatterns = [
    # Ruta para acceder al panel de administración de Django (ej. /admin/)
    path('admin/', admin.site.urls),
    
    # Ruta base para la API. 
    # Cualquier URL que comience con '/api/' será delegada y resuelta por el archivo 'urls.py' dentro de la app 'productos'
    path('api/', include('productos.urls')),
]