from django.contrib import admin
from .models import etudiant, memoire, soutenance, enseignant, stage, entreprise, parcours, mention, annee_academique

# Register your models here.
class etudiantAdmin(admin.ModelAdmin): 
  list_display =['nom', 'prenom', 'matricule']

class memoireAdmin(admin.ModelAdmin): 
  list_display =['titre', 'memoire_doc', 'etudiant',] 
class soutenanceAdmin(admin.ModelAdmin): 
  list_display =['jury', 'date_sout', 'mention_sout',] 

admin.site.register(etudiant,etudiantAdmin)
admin.site.register(memoire, memoireAdmin)
admin.site.register(soutenance, soutenanceAdmin)
admin.site.register(enseignant)
admin.site.register(stage)
admin.site.register(entreprise)
admin.site.register(parcours)
admin.site.register(mention)
admin.site.register(annee_academique)