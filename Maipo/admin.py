from django.contrib import admin
from .models import Productor,Producto,Transportista,clienteExterno,clienteLocal,subasta

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio']


admin.site.register(Productor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Transportista)
admin.site.register(clienteExterno)
admin.site.register(clienteLocal)
admin.site.register(subasta)

