from django.db import models

# Define la estructura de cada producto que se guarda en la base de datos.
class Producto(models.Model):
    # Datos descriptivos y comerciales del producto.
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    # Django asigna la fecha automáticamente al crear el producto.
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
# str = texto plano que representa el objeto, útil para mostrarlo en el panel de administración y en otras representaciones. 
#(self) = hace referencia a la instancia actual del modelo Producto.
    def __str__(self):
        # Muestra el nombre del producto en el panel y en otras representaciones.
        return self.nombre