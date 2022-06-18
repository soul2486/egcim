from django.contrib import admin
from .models import etudiant, memoire, soutenance, enseignant, stage, entreprise, parcours, mention, annee_academique

# Register your models here.
admin.site.register(etudiant)
admin.site.register(memoire)
admin.site.register(soutenance)
admin.site.register(enseignant)
admin.site.register(stage)
admin.site.register(entreprise)
admin.site.register(parcours)
admin.site.register(mention)
admin.site.register(annee_academique)