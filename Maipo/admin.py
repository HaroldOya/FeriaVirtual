from django.contrib import admin
from .models import Productor,Producto,Transportista,clienteExterno,clienteLocal

admin.site.register(Productor)
admin.site.register(Producto)
admin.site.register(Transportista)
admin.site.register(clienteExterno)
admin.site.register(clienteLocal)

