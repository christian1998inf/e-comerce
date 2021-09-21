from django.contrib import admin

from gestionProductos.models import Contacto, Producto , Pedidos

# Register your models here.


admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Pedidos)