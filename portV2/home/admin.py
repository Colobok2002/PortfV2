from django.contrib import admin
from .models import Projekt


class ProjektAdmin(admin.ModelAdmin):

    list_display = ['name','utl_git']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Projekt,ProjektAdmin)
