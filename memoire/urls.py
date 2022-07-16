from re import search
from django.urls import URLPattern, path, re_path
from .views import * 
from taggit.models import Tag 
# from .views import index, 
# from views import depot
urlpatterns = [
    path('',index, name = "index"),
    path('depot/',depot, name = "depot"),
    path('ajouter_enseignant/',ajouter_ens, name = "ajouter_ens"),
    path('connexion/',connexion, name = "connexion"),
    path('tag/<slug:tag_slug>',consulter, name = "memoire_tag"),
    path('ajouter_parcours/',ajouter_parcours, name = "ajouter_parcours"),
    path('ajouter_entreprise/',ajouter_entreprise, name = "ajouter_entreprise"),
    path('list_entreprise/',list_entreprise, name = "list_entreprise"),
    path('list_enseignant/',list_enseignant, name = "list_enseignant"),
    path('deconnexion/',deconnexion, name = "deconnexion"),
    path('ajouter_mention/',ajouter_mention, name = "ajouter_mention"),
    path('ajouter_annee/',ajouter_annee, name = "ajouter_annee"),
    path('search_result/',search, name = "search"),
    path('recherche/',recherche, name = "recherche"),
    # path('filtre/',filtre, name = "filtre"),
    path(r'^list$',filtre, name = "filtre"),
    path('get_filtre/<str:filtre>/',get_filtre, name = "get_filtre"),
    # path('get_etudiant/<str:id_etudiant>/',get_etudiant, name = "get_etudiant"),
    # path('message/',feedback, name = "feedback"),
    path('consulter/',consulter, name = "consulter"),
    path('tag/(?P<slug>[-a-zA-Z0-9_]+)\\Z',consulter2, name = "tagget"),
    re_path(r'^(?P<id_memoire>[0-9]+)/$', detail, name='detail'),
    path('modif_ent/<int:id_entreprise>/', modif_ent, name='modif_ent'),
    path('parcours/<str:id_parcours>/', getparcours, name='parcours'),
    path('delete_ent/<int:id_entreprise>/', delete_ent, name='delete_ent'),
    path('modif_ens/<int:id_enseignant>/', modif_ens, name='modif_ens'),
    path('delete_ens/<int:id_enseignant>/', delete_ens, name='delete_ens'),
    path(r'^(?P<memoire_id>[0-9]+)/$', load_doc, name='load_doc'),
    re_path(r'^(?P<memoire_id>[0-9]+)/$', view_doc, name='view_doc'),
    
    # re_path(r'^search/$', search, name='search'),

]