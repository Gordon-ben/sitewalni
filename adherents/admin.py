from django.contrib import admin
from .models import Adherent


@admin.register(Adherent)
class AdherentAdmin(admin.ModelAdmin):
    list_display  = ('prenoms', 'noms', 'telephone', 'province', 'commune', 'date_adhesion', 'date_enregistrement')
    search_fields = ('noms', 'prenoms', 'telephone', 'province')
    list_filter   = ('province', 'qualite')
    ordering      = ('-date_enregistrement',)