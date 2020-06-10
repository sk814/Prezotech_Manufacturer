from django.contrib import admin
from .models import Manu

class ManuAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Manu, ManuAdmin)
