from tkinter import CASCADE
from weakref import proxy
from django.db import models

#Create your models here.
class etudiant(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    matricule = models.CharField(max_length=20)
    parcours = models.ForeignKey('parcours', on_delete=models.CASCADE)
    # enseignant = models.ForeignKey('enseignant', on_delete=models.CASCADE)
    stage = models.ForeignKey('stage', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
class annee_academique(models.Model):
    annee = models.CharField(max_length=100)
    def __str__(self):
        return self.annee
class memoire(models.Model):
    titre = models.CharField(max_length=100)
    mot_cle = models.CharField(max_length=100)
    resume = models.TextField()
    memoire_doc = models.FileField(upload_to='document/%Y/%m/%d/', blank = True)
    annee_academique =  models.ForeignKey('annee_academique', on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    # create_at = models.DateTimeField()
    etudiant = models.ForeignKey('etudiant', on_delete=models.CASCADE)
    soutenance = models.OneToOneField("soutenance",related_name='memoire', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.titre
class enseignant(models.Model):
    nom_ens = models.CharField(max_length=20)
    prenom_ens = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
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
    encadreur_ind =models.CharField(max_length=20, blank=True) 
    president = models.ForeignKey(president, related_name='president', on_delete=models.CASCADE)
    encadreur = models.ForeignKey(encadreur, related_name='encadreur', on_delete=models.CASCADE)
    examinateur = models.ForeignKey(examinateur, related_name='examinateur', on_delete=models.CASCADE)
class soutenance(models.Model):
    mention_choice = [
        ('Excellent', 'Excellent'),
        ('Tres Bien', 'Tres Bien'),
        ('Bien', 'Bien'),
        ('Assez Bien', 'Assez Bien'),
    ]
    salle = models.CharField(max_length=50)
    jury = models.ForeignKey(jury, on_delete=models.CASCADE)
    note = models.FloatField(max_length=20)
    mention_sout = models.CharField(max_length=20, choices=mention_choice)
    # type_sout =  models.CharField(max_length=20)
    date_sout = models.DateField()
    def __str__(self):
        return self.mention_sout

class stage(models.Model):
    type_stage = models.CharField(max_length=20)
    date_debut = models.DateField(auto_now=False)
    date_fin = models.DateField(auto_now=False)
    entreprise = models.ForeignKey('entreprise', on_delete=models.CASCADE)
    def __str__(self):
        return self.type_stage
class entreprise(models.Model):
    nom_ent = models.CharField(max_length=20)
    lieu = models.CharField(max_length=20) 
    def __str__(self):
        return self.nom_ent +' ('+ self.lieu +')'

class mention(models.Model):
    mention = models.CharField(max_length=50)

    def __str__(self):
        return self.mention

class parcours(models.Model):
    parcours = models.CharField(max_length=50)
    mention = models.ForeignKey(mention, on_delete=models.CASCADE)
    def __str__(self):
        return self.parcours
    def __unicode__(self):
        return self.parcours
