from tkinter import CASCADE
from weakref import proxy
from django.db import models
from taggit.managers import TaggableManager 
import datetime
#Create your models here.
class etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    matricule = models.CharField(max_length=20)
    parcours = models.ForeignKey('parcours', on_delete=models.CASCADE)
    # enseignant = models.ForeignKey('enseignant', on_delete=models.CASCADE)
    stage = models.ForeignKey('stage', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
class annee_academique(models.Model):
    annee = models.DateField(unique=True)   
    def __str__(self):
        # self.objects.filter(self__year = self.year)
        ann = self.annee.strftime("%Y")
        # ann_cour = int(ann)
        # ann_sui = ann + 1
        return ann
class memoire(models.Model):
    titre = models.CharField(max_length=1000)
    mot_cle = TaggableManager()
    resume = models.TextField()
    memoire_doc = models.FileField(upload_to='document/%Y/%m/%d/', blank = True)
    annee_academique =  models.ForeignKey('annee_academique', on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=False, max_length=100)
    # create_at = models.DateTimeField()
    etudiant = models.ForeignKey('etudiant', on_delete=models.CASCADE)
    soutenance = models.OneToOneField("soutenance",related_name='memoire', on_delete=models.CASCADE)
    # tags = TaggableManager()
   
    def __str__(self):
        return self.titre
class enseignant(models.Model):
    grade_choice = [
        ('Professeur', 'Professeur'),
        ('Maitre de conference', 'Maitre de conference'),
        ('Chargé de cours', 'chargé de cours'),
        ('Assistant(e)', 'Assistant(e)'),
       
    ]
    nom_ens = models.CharField(max_length=100)
    prenom_ens = models.CharField(max_length=100, blank = True)
    grade = models.CharField(max_length=20, choices=grade_choice)
    def __str__(self):
        return self.nom_ens
    def __unicode__(self):
        return self.parcours
class president(enseignant):
    class Meta:
        proxy = True
    def __unicode__(self):
        return self.nom_ens
class encadreur(enseignant):
    class Meta:
        proxy = True
    def __unicode__(self):
        return self.nom_ens
class examinateur(enseignant):
    class Meta:
        proxy = True
    def __unicode__(self):
        return self.nom_ens

class jury(models.Model):
    encadreur_ind =models.CharField(max_length=100, blank=True) 
    president = models.ForeignKey(president, related_name='president', on_delete=models.CASCADE)
    encadreur = models.ForeignKey(encadreur, related_name='encadreur', on_delete=models.CASCADE)
    examinateur = models.ForeignKey(examinateur, related_name='examinateur', on_delete=models.CASCADE)
    def __unicode__(self):
        return self.encadreur_ind
class soutenance(models.Model):
    mention_choice = [
        ('Excellent', 'Excellent'),
        ('Tres Bien', 'Tres Bien'),
        ('Bien', 'Bien'),
        ('Assez Bien', 'Assez Bien'),
    ]
    salle = models.CharField(max_length=100, blank=True)
    jury = models.ForeignKey(jury, on_delete=models.CASCADE)
    note = models.FloatField(max_length=20, blank=True, null=True)
    mention_sout = models.CharField(max_length=100, choices=mention_choice, blank=True)
    # type_sout =  models.CharField(max_length=20)
    date_sout = models.DateField()
    def __str__(self):
        return self.mention_sout

class stage(models.Model):
    type_stage = models.CharField(max_length=100)
    date_debut = models.DateField(auto_now=False)
    date_fin = models.DateField(auto_now=False)
    entreprise = models.ForeignKey('entreprise', on_delete=models.CASCADE)
    def __str__(self):
        return self.type_stage
class entreprise(models.Model):
    nom_ent = models.CharField(max_length=1000)
    lieu = models.CharField(max_length=1000) 
    def __str__(self):
        return self.nom_ent +' ('+ self.lieu +')'

class mention(models.Model):
    mention = models.CharField(max_length=50)

    def __str__(self):
        return self.mention

class parcours(models.Model):
    parcours = models.CharField(max_length=100)
    mention = models.ForeignKey(mention, on_delete=models.CASCADE)
    def __str__(self):
        return self.parcours
    def __unicode__(self):
        return self.parcours
