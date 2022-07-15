from dataclasses import field, fields
from pyexpat import model
from time import strftime
from django.forms import DateTimeInput, TextInput, Textarea, DateInput, FileInput, NumberInput, ModelForm, widgets
from django import forms
from .models import *
PARCOURS_CHOICES = [('parcours1','parcours1'),('parcours2','parcours2'),('parcours3','parcours3'),('parcours4','parcours4')]
# parcour = parcours()
# class parcoursSelect(forms.Select):
#     def create_option(self, parcours, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex, attrs)
#         if value:
#             option['attrs']['data-parcours'] = value.instance.parcours
#         return option
class etudiantForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ('nom','prenom', 'matricule', 'parcours')
        widgets = {
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'prenom':forms.TextInput(attrs={'class':'form-control'}),
            'matricule':forms.TextInput(attrs={'class':'form-control'}),
            'parcours':forms.Select(attrs={'class':'form-control'}),
            # 'enseignant':forms.Select(attrs={'class':'form-control'}),
            # 'stage':forms.Select(attrs={'class':'form-control'}),
        }
    
class enseignantForm(forms.ModelForm):
    class Meta:
        model = enseignant
        fields = ['nom_ens','prenom_ens', 'grade']
        widgets = {
            'nom_ens':TextInput(attrs={'class':'form-control'}),
            'prenom_ens':TextInput(attrs = {'class':'form-control'}),
            'grade':forms.Select(attrs = {'class':'form-control'}),
        }
    # nom_ens = forms.CharField(
    #     label = 'Nom',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=True)

    # prenom_ens = forms.CharField(
    #     label = 'Prenom',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=False)
    # grade = forms.CharField(
    #     label = 'Grade',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=True)
    


    # titre = forms.CharField(
    #     label = 'Titre',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=True)

    # mot_cle = forms.CharField(
    #     label = 'Mot_cle',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=True)
    # resume = forms.CharField(
    #     label = 'Resume',
    #     max_length= 500000,
    #     widget = forms.Textarea(attrs = {'class': 'form-control'}),
    #     required=True)
    # annee_academique = forms.DateField(
    #     label = 'Anne_academique',
    #     widget = forms.DateInput(attrs = {'class': 'form-control', 'type': 'date'}),
    #     required=False)
    # memoire =forms.FileField(
    #     label= 'Memoire',
    #     widget =forms.FileInput(
    #         attrs = {'class': 'form-control'}
    #     ),
    #      max_length=100, 
    #      required=False)
    

class soutenanceForm(forms.ModelForm):
    class Meta:
        model = soutenance
        fields = ('salle', 'note', 'mention_sout', 'date_sout')
        widgets = {
            'salle':TextInput(attrs={'class':'form-control'}),
            'note':NumberInput(attrs={'class':'form-control'}),
            # 'jury':TextInput(attrs={'class':'form-control'}),
            'mention_sout':forms.Select(attrs={'class':'form-control'}),
            # 'type_sout':TextInput(attrs={'class':'form-control'}),
            'date_sout':DateInput(attrs = {'class':'form-control', 'type':'date'}),
            
        }

    #     salle = forms.CharField(
    #     label = 'Salle',
    #     max_length= 50,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}),
    #     required=True)

    # date_sout = forms.DateField(
    #     label = 'Date',
    #     # max_length= 50,
    #     widget = forms.DateInput(attrs = {'class': 'form-control', 'type': 'date'}),
    #     required=False)
    # note = forms.DecimalField(
    #     label = 'Note',
    #     # max_length= 50,
    #     widget = forms.NumberInput(attrs = {'class': 'form-control'},),
    #     required=True)
    # jury = forms.CharField(
    #     label = 'jury',
    #     max_length=100,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}), 
    #     required=False)
    # mention_sout = forms.CharField(
    #     label = 'Mention',
    #     max_length=100,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}), 
    #     required=False)
    # type_sout = forms.CharField(
    #     label = 'Type de soutenance',
    #     max_length=20,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'}), 
    #     required=True)
class stageForm(forms.ModelForm):
    class Meta:
        model = stage
        fields = ('type_stage', 'date_debut', 'date_fin', 'entreprise')
        widgets = {
            'type_stage':TextInput(attrs={'class':'form-control'}),
            'date_debut':DateInput(attrs = {'class':'form-control', 'type':'date'}),
            'date_fin':DateInput(attrs = {'class':'form-control', 'type':'date'}),
            'entreprise':forms.Select(attrs={'class':'form-control'}),
        }
    # type_stage = forms.CharField(
    #     label= 'Type_stage',
    #     max_length=20,
    #     widget = forms.TextInput(attrs = {'class':'form-control'}),
    #     required=False)
    # date_debut = forms.DateField(
    #     label = 'Date_debut',
    #     # max_length= 50,
    #     widget = forms.DateInput(attrs = {'class': 'form-control', 'type': 'date'}),
    #     required=False)
    # date_fin = forms.DateField(
    #     label = 'Date_fin',
    #     # max_length= 50,
    #     widget = forms.DateInput(attrs = {'class': 'form-control', 'type': 'date'}),
    #     required=False)
class entrepriseForm(forms.ModelForm):
    class Meta :
        model = entreprise
        fields = ('nom_ent', 'lieu')
        widgets = {
            'nom_ent':TextInput(attrs={'class':'form-control'}),
            'lieu':TextInput(attrs={'class':'form-control'}),
        }
class anneeForm(forms.ModelForm):
    class Meta :
        model = annee_academique
        fields = ['annee']
        widgets = {
            'annee':DateInput(attrs={'type':'date','class':'form-control'}, format=strftime('%Y'))
            
        }
#     nom_ent = forms.CharField(
#         label= 'Nom_entreprise',
#         max_length=20,
#         widget = forms.TextInput(attrs = {'class':'form-control'}),
#         required=False)
#     lieu = forms.CharField(
#         label= 'Lieu_entreprise',
#         max_length=20,
#         widget = forms.TextInput(attrs = {'class':'form-control'}),
#         required=False)
class mentionForm(forms.ModelForm):
    class Meta:
        model = mention
        fields = ['mention']
        widgets = {
            'mention':TextInput(attrs={'class':'form-control'}),
        }
# class anneeForm(forms.ModelForm):
#     class Meta:
#         model = annee_academique
#         fields = ['annee']
#         widgets = {
#             'annee':TextInput(attrs={'class':'form-control'}),
#         }
    # mention = forms.CharField(
    #     label = 'mention',
    #     max_length=20, 
    #     widget = forms.TextInput(attrs = {'class':'form-control'}),
    #     required=False)

class parcoursForm(forms.ModelForm):
    class Meta:
        model = parcours
        fields = ['parcours', 'mention']
        widgets = {
            'parcours':TextInput(attrs={'class':'form-control'}),
            'mention':forms.Select(attrs={'class':'form-control'}),
        }
    # parcours = forms.ChoiceField(
    #     label = 'parcours',
        
    #     widget = forms.Select(attrs = {'class':'form-select'}),

    #     choices = PARCOURS_CHOICES,
    #     # max_length=20, 
    #     required=False)
class memoireForm(forms.ModelForm):
    class Meta:
        model = memoire
        fields = ('titre','mot_cle', 'resume','memoire_doc','annee_academique')
        widgets = {
            'titre':TextInput(attrs={'class':'form-control'}),
            'mot_cle':forms.TextInput(attrs = {'class':'form-control'}),
            'resume':Textarea(attrs = {'class':'form-control'}),
            'memoire_doc':FileInput(attrs = {'class':'form-control'}),
            'annee_academique':forms.Select(attrs={'class':'form-control'}),
            # 'tags':TextInput(attrs = {'class':'form-control'}),

            # 'date_creation': DateInput(),
        }

class juryForm(forms.ModelForm):
    class Meta:
        model = jury
        fields = ('president', 'examinateur', 'encadreur', 'encadreur_ind')
        widgets = {
            'encadreur_ind':TextInput(attrs={'class':'form-control'}),
            'president':forms.Select(attrs={'class':'form-control'}),
            'examinateur':forms.Select(attrs={'class':'form-control'}),
            'encadreur':forms.Select(attrs={'class':'form-control'}),
        }