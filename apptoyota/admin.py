from django.contrib import admin
from apptoyota.models import toyotas
# Register your models here.
class toyotasAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo','contenido','imagen','creado', 'actualizado')

admin.site.register(toyotas, toyotasAdmin)
