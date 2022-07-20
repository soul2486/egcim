from django.forms import DateTimeInput, TextInput, Textarea, DateInput, FileInput, NumberInput, ModelForm, widgets
import django_filters
from .models import memoire

class memoireFilter(django_filters.FilterSet):
    choix = memoire.objects.all()
    # annee_year = django_filters.ChoiceFilter(field_name='annee_academique', lookup_expr='year')
    # annee_year__gt = django_filters.NumberFilter(field_name='annee_academique', lookup_expr='year__gt')
    # annee_year__lt = django_filters.NumberFilter(field_name='annee_academique', lookup_expr='year__lt')
    # etudiant__nom = django_filters.ChoiceFilter(lookup_expr='icontains')
    # mot_cle = django_filters.ChoiceFilter(field_name='mot_cle__name',lookup_expr='icontains')
    class Meta:
        model = memoire
        fields = {'etudiant', 'etudiant__parcours', 'etudiant__stage__entreprise', 'annee_academique', 'mot_cle__name'}
        # filter_overrides = {
        #      models.CharField: {
        #          'filter_class': django_filters.CharFilter,
        #          'extra': lambda f: {
        #              'lookup_expr': 'icontains',
        #          },
        #      },
        # }