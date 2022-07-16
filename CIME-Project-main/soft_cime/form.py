from socket import fromshare
from django import forms
from .models import *

class ContribuableForm(forms.ModelForm):
    class Meta:
        model = contribuable
        fields = ('NIU','raison_social','activite','regime_impot','telephone','arrondissement','departement','ug','sous_secteur')
        widgets = {
            'NIU':forms.TextInput(attrs={'class':'form-control'}),
            'raison_social':forms.TextInput(attrs={'class':'form-control'}),
            'activite':forms.TextInput(attrs={'class':'form-control'}),
            'regime_impot':forms.TextInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'regime_impot':forms.Select(attrs={'class':'form-control'}),
            'arrondissement':forms.TextInput(attrs={'class':'form-control'}),
            'departement':forms.Select(attrs={'class':'form-control'}),
            'ug':forms.Select(attrs={'class':'form-control'}),
            'sous_secteur':forms.Select(attrs={'class':'form-control'}),
        }
        
class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration
        fields = ('num_avis','chiffre_affaire','date_limite','contribuable')
        widgets = {
            'num_avis':forms.TextInput(attrs={'class':'form-control'}),
            'chiffre_affaire':forms.TextInput(attrs={'class':'form-control'}),
            'date_limite':forms.TextInput(attrs={'class':'form-control'}),
            'contribuable':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
class DeclarationImpotForm(forms.ModelForm):
    class Meta:
        model = Impot_Declare
        fields = ('impot','montant')
        widgets = {
            'impot':forms.Select(attrs={'class':'form-control'}),
            'montant':forms.TextInput(attrs={'class':'form-control'}),
            
        }
