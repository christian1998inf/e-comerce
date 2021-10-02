from django.contrib import admin

from gestionProductos.models import Contacto, Producto , Pedidos

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Correo", "Tema")
    search_fields=("Nombre", "Tema")

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Producto)
admin.site.register(Pedidos)