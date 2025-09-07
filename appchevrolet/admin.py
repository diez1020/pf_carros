from django.contrib import admin
from appchevrolet.models import chevys
# Register your models here.
class chevysAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo','contenido','imagen','creado', 'actualizado')

admin.site.register(chevys, chevysAdmin)