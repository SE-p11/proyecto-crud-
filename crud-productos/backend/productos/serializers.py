from rest_framework import serializers
from .models import Producto

# Convierte productos entre instancias de Django y datos JSON de la API.
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # Incluye en la API todos los campos definidos en el modelo Producto.
        fields = '__all__'