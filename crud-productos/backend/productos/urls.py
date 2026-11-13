from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# El router genera automáticamente todas las rutas CRUD para este ViewSet.
router = DefaultRouter()
# Registra el recurso 'productos' asociado a su respectivo ViewSet
router.register(r'productos', ProductoViewSet)

# Incluye las rutas generadas por el router en las URLs de esta aplicación.
urlpatterns = [
    # Incluye todas las URLs automáticas creadas por el router (ej. /productos/, /productos/<id>/)
    path('', include(router.urls)),
]