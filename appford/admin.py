from django.contrib import admin
from appford.models import fords
# Register your models here.
class fordAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo','contenido','imagen','creado', 'actualizado')

admin.site.register(fords, fordAdmin)