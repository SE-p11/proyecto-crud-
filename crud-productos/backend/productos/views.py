from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# Expone las operaciones de listar, crear, consultar, actualizar y eliminar productos.
class ProductoViewSet(viewsets.ModelViewSet):
    # Define los productos sobre los que puede operar la API.
    queryset = Producto.objects.all()
    # Define cómo se convierten los productos a/desde los datos de las solicitudes.
    serializer_class = ProductoSerializer