from django.contrib import admin
from apphome.models import sponsor
# Register your models here.
class sponsorAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo', 'imagen','creado', 'actualizado')

admin.site.register(sponsor, sponsorAdmin)