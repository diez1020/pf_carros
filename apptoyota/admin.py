from django.contrib import admin
from apptoyota.models import hoteles
# Register your models here.
class hotelesAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('nombre','distancia','imagen','precio','creado', 'actualizado')

admin.site.register(hoteles, hotelesAdmin)

