from django.contrib import admin
from appcontacto.models import contacto
# Register your models here.
class contactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','imagen',)

admin.site.register(contacto, contactoAdmin)