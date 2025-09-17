from django.contrib import admin
from appchevrolet.models import vehiculos
# Register your models here.
class vehiculosAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('modelo','marca','categoria','motor','contenido','imagen','creado', 'actualizado')

admin.site.register(vehiculos, vehiculosAdmin)