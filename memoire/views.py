from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchVector,SearchRank, TrigramSimilarity
from django.core.paginator import Paginator
from django.db.models.functions import Greatest
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.template import context
from .filters import memoireFilter
from django.template.defaultfilters import slugify
from .models import etudiant, memoire, soutenance, enseignant, stage, entreprise, parcours, mention
from .forms import etudiantForm, enseignantForm, memoireForm, soutenanceForm, entrepriseForm, anneeForm, stageForm, parcoursForm, mentionForm, juryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.db.models import Count 
# Create your views here.
def index(request):
    parcour = parcours.objects.all()
    memoires = memoire.objects.all()
    list_count = []
    for i in parcour:
        l = []
        c = memoire.objects.filter(etudiant__in = etudiant.objects.filter(parcours = i)).count()
        l.append(i)
        l.append(c)
        list_count.append(l)

    nb_memoire =memoire.objects.order_by('etudiant__parcours__parcours').count()
    context = {'parcours':parcour,
                'memoires':memoires,
                'nb':nb_memoire,
                'list_count' : list_count,
    }
    return render(request,"home.html", context)

def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('depot')
        else:
            messages.success(request, "erreur d'authentification !")
            return redirect('connexion')
    return render(request, 'connexion.html')
@login_required(login_url='connexion')
def deconnexion(request):
    logout(request)
    return redirect('index')
@login_required(login_url='connexion')
def depot(request):
    # messagess = messages.success(request, 'empty')
    if request.method == "POST":
        form_etud  = etudiantForm(request.POST)
        form_soutenance = soutenanceForm(request.POST)
        form_memoire = memoireForm(request.POST, request.FILES)
        form_stage = stageForm(request.POST)
        form_jury = juryForm(request.POST)
        # form_entreprise = entrepriseForm(request.POST)
        if (form_etud.is_valid() and form_soutenance.is_valid() and form_memoire.is_valid() and form_stage.is_valid()):
            form_etud  = etudiantForm(request.POST).save(commit=False)
            form_soutenance = soutenanceForm(request.POST).save(commit = False)
            form_jury = juryForm(request.POST).save()
            form_memoire2 = form_memoire.save(commit=False)
            form_stage = stageForm(request.POST).save(commit=False)
            # form_entreprise = entrepriseForm(request.POST).save()    
            # form_stage.entreprise = form_entreprise
            form_soutenance.jury = form_jury
            form_soutenance.save()
            form_stage.save()
            form_etud.stage = form_stage
            form_etud.save()
            form_memoire2.soutenance = form_soutenance
            form_memoire2.etudiant = form_etud
            form_memoire2.slug = slugify(form_memoire2.titre)
            # form_memoire.tags = request.GET.get('mot_cle')
            form_memoire2.save()
            # form_memoire.save(commit= False)
            form_memoire.save_m2m()

            form_etud.stage = form_stage
            form_etud.save()
            
            context = {
            'form_etud':etudiantForm(),
            'form_memoire':memoireForm(),
            'form_soutenance':soutenanceForm(),
            'form_stage':stageForm(),
            # 'form_entreprise':entrepriseForm(),
            'form_jury':juryForm()
            }
            # redirect('depot.html')
            messages.success(request, 'empty')
            return render(request,'depot.html', context)
        else:
            context = {
                # 'errors_etud':form_etud.errors.items(),
                # 'errors_soutenance':form_soutenance.errors.items(),
                # 'errors_memoire':form_memoire.errors.items(),
                # 'errors_stage':form_stage.errors.items(),
                # 'errors':form_entreprise.errors.items(),
            }
            return render(request,'depot.html', context)
    else:
        form_etud = etudiantForm()
        form_ens = enseignantForm()
        form_memoire = memoireForm()
        form_soutenance = soutenanceForm()
        form_stage = stageForm()
        # form_entreprise = entrepriseForm()
        form_parcours = parcoursForm()
        form_jury  = juryForm()
    context = {
        'form_etud':form_etud,
        'form_ens':form_ens,
        'form_memoire':form_memoire,
        'form_soutenance':form_soutenance,
        'form_stage':form_stage,
        # 'form_entreprise':form_entreprise,
        'form_parcours':form_parcours,
        'form_jury':form_jury,
        # 'errors':form_entreprise.errors.items(),
        }
    # messages.success(request, 'empty')
    return render(request,'depot.html', context)
def consulter(request):
    memoires = memoire.objects.order_by('-date_creation')[:12]
    # comons_tag = memoire.mot_cle.most_common()
    f = memoireFilter(request.GET, queryset=memoire.objects.order_by('-date_creation'))
    formated_memoires = ["<li>{}</li>".format(memoire.titre) for memoire in memoires]
    paginator = Paginator(f.qs,12)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'memoires':page_object,'filter':f}
    return render(request,'consulter.html', context)
def consulter2(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    memoires = memoire.objects.order_by('-date_creation')[:12]
    comons_tag = memoire.mot_cle.most_common()
    f = memoireFilter(request.GET, queryset=memoire.objects.filter(mot_cle=tag))
    formated_memoires = ["<li>{}</li>".format(memoire.titre) for memoire in memoires]
    paginator = Paginator(f.qs,12)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'memoires':page_object,'filter':f}
    return render(request,'consulter.html', context)
def detail(request, id_memoire,  slug = None):
    memoires = memoire.objects.get(pk = id_memoire)
    memoires_tags_ids = memoire.mot_cle.values_list('id', flat=True)
    similar_memoire = memoire.objects.filter(mot_cle__in=memoires_tags_ids).exclude(id=memoires.id)
    similar_memoire = similar_memoire.annotate(same_mot_cle= Count('mot_cle')).order_by('same_mot_cle')[:2]
    tag = None
    memoirestag = None
    if slug:
        tag = get_object_or_404(Tag, slug=slug)
        memoirestag = memoire.objects.filter(mot_cle__in = [tag][:3])
        # mot_clee = memoires.mot_cle
        # memoires_simi = memoire.objects.filter(mot_cle = mot_clee )[:12]
        # formated_memoires = ["<li>{}</li>".format(memoire.titre) for memoire in memoires_simi]
        context = {'memoires':memoires, 'memoirestag':memoirestag, 'tag':tag, 'similar_memoire':similar_memoire}
    else:
        context = {'memoires':memoires, 'memoirestag':memoirestag, 'tag':tag, 'similar_memoire':similar_memoire}
    return render(request, 'detail2.html', context)
def getparcours(request, id_parcours):
    parc = parcours.objects.get(parcours=id_parcours)
    memoires = memoire.objects.filter(etudiant__parcours__parcours= parc)[:12]
    # comons_tag = memoire.tags.most_common()[:10]
    f = memoireFilter(request.GET, queryset= memoire.objects.filter(etudiant__parcours__parcours= parc))
    formated_memoires = ["<li>{}</li>".format(memoire.titre) for memoire in memoires]
    paginator = Paginator(f.qs,12)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'memoires':page_object,'filter':f,}
    return render(request,'consulter.html', context)
def load_doc (request, memoire_id):
    id = int(memoire_id)
    # id = id/10
    memoires = memoire.objects.get(pk = id)
    fs = FileSystemStorage()
    filename ='/egcim/{}'.format(memoires.memoire_doc)
    # print(filename)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type ='application/pdf' )
            response['Content-Disposition'] = 'attachment; filename = "pdf.pdf"'
            return response
    else:   
        return HttpResponseNotFound('the pdf is not found {}'.format(filename))
    return render(request)
def view_doc (request, memoire_id):
    id = int(memoire_id)
    # id = id/10
    memoires = memoire.objects.get(pk=id)
    fs = FileSystemStorage()
    filename ='/egcim/{}'.format(memoires.memoire_doc)
    # print(filename)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type ='application/pdf' )
            response['Content-Disposition'] = 'inline; filename = "pdf.pdf"'
            return response
    else:   
        return HttpResponseNotFound('the pdf is not found {}'.format(filename))
    return render(request)
# def feedback(request):
#     return render(request, 'reponse.html')
def ajouter_ens(request):
    if request.method == "POST":
        form_ens  = enseignantForm(request.POST).save()
        messages.success(request, 'empty')
        form_ens = enseignantForm()
        return render(request,'ajout_ens.html')
    else:
        form_ens = enseignantForm()
        context = {'form_ens':form_ens}
        return render(request,'ajout_ens.html', context)
def ajouter_parcours(request):
    if request.method == "POST":
        form_parcours  = parcoursForm(request.POST).save()
        messages.success(request, 'empty')
        form_parcours = parcoursForm()
        return render(request,'ajout_parcours.html')
    else:
        form_parcours = parcoursForm()
        context = {'form_parcours':form_parcours}
    return render(request,'ajout_parcours.html', context)

def list_entreprise(request):
    entreprises = entreprise.objects.order_by('nom_ent')
    context = {'entreprise':entreprises, 'i':1}
    return render(request, 'list_ent.html', context)
def list_enseignant(request):
    enseignants = enseignant.objects.order_by('nom_ens')
    context = {'enseignants':enseignants, 'i':1}
    return render(request, 'list_ens.html', context)
def delete_ent(request, id_entreprise):
    entreprises =  entreprise.objects.get(pk = id_entreprise)
    entreprises = entreprises.delete()
    messages.success(request, 'empty')
    context = {'entreprise':entreprises, 'i':1}
    return render(request, 'delete_ent.html', context)
def delete_ens(request, id_enseignant):
    enseignants =  enseignant.objects.get(pk = id_enseignant)
    enseignants = enseignants.delete()
    messages.success(request, 'empty')
    context = {'entreprise':enseignants, 'i':1}
    return render(request, 'delete_ent.html', context)
def modif_ent(request, id_entreprise):
    if request.method == 'POST':
        entreprises = entreprise.objects.get(pk = id_entreprise)
        nom_ent = request.POST.get('nom')
        lieu = request.POST.get('lieu')
        entreprises.nom_ent = nom_ent
        entreprises.lieu = lieu
        entreprises.save()
        messages.success(request, 'empty')
        return render(request, 'modif_ent.html')
    else:
        entreprises = entreprise.objects.get(pk = id_entreprise)
        context = {'entreprises':entreprises}
        return render(request, 'modif_ent.html', context)
def modif_ens(request, id_enseignant):
    if request.method == 'POST':
        enseignants = enseignant.objects.get(pk = id_enseignant)
        nom_ens = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        enseignants.nom_ens = nom_ens
        enseignants.prenom_ens = prenom
        enseignants.grade = prenom
        enseignants.save()
        messages.success(request, 'empty')
        return render(request, 'modif_ens.html')
    else:
        enseignants = enseignant.objects.get(pk = id_enseignant)
        context = {'enseignants':enseignants}
        return render(request, 'modif_ens.html', context)
def ajouter_entreprise(request):
    if request.method == "POST":
        form_entreprise  = entrepriseForm(request.POST).save()
        messages.success(request, 'empty')
        form_entreprise = entrepriseForm()
        return render(request,'ajout_ent.html')
    else:
        form_entreprise = entrepriseForm()
        context = {'form_ent':form_entreprise}
        return render(request,'ajout_ent.html', context)
def ajouter_mention(request):
    if request.method == "POST":
        form_mention  = mentionForm(request.POST).save()
        messages.success(request, 'empty')
        form_mention = mentionForm()
        return render(request,'ajout_mention.html')
    else:
        form_mention = mentionForm()
        context = {'form_mention':form_mention}
        return render(request,'ajout_mention.html', context)
def ajouter_annee(request):
    if request.method == "POST":
        form_annee  = anneeForm(request.POST).save()
        messages.success(request, 'empty')
        form_annee = anneeForm()
        return render(request,'ajout_annee.html')
    else:
        form_annee = anneeForm()
        context = {'form_annee':form_annee}
        return render(request,'ajout_annee.html', context)

def search (request):
    search = request.GET.get('search')
    vector = SearchVector('titre','mot_cle', 'resume', 'etudiant__nom', 'etudiant__parcours__parcours')
    query = SearchQuery(search)
    # memoires = memoire.objects.annotate(search = vector).filter(search = query)
    # memoires = memoire.objects.annotate(rank = SearchRank(vector, query)).filter(rank__gte = 0.001).order_by('-rank')
    memoires = memoire.objects.annotate(similarity=Greatest(
                                                        TrigramSimilarity('titre', search),
                                                        TrigramSimilarity('etudiant__nom', search),
                                                        TrigramSimilarity('etudiant__prenom', search),
                                                        # TrigramSimilarity('mot_cle__name', search),
                                                        TrigramSimilarity('etudiant__parcours__parcours', search),)).filter(similarity__gte= 0.1).order_by('-similarity')

    # memoires = memoire.objects.filter(Q(titre__icontains = search)|
    #                                   Q(mot_cle__icontains = search)|
    #                                   Q(annee_academique__icontains = search)|
    #                                   Q(etudiant__nom__icontains = search))
    # memoires =  memoire.objects.filter(Q(titre__search = search)|
    #                                    Q(mot_cle__search = search)|                                        
    #                                    Q(etudiant__nom__search = search))
    results_number = memoires.count()
    message = f'{results_number} resultats :'
    if results_number <= 1:
        message = f'{results_number} resultat :'
    context = {
        'memoires':memoires,
        'message':message,
    }
    return render(request, 'search_results.html', context)
def recherche(request):
    search = request.GET.get('search2')
    if search:
        vector = SearchVector('titre','mot_cle', 'resume', 'etudiant__nom', 'etudiant')
        query = SearchQuery(search)
        # memoires = memoire.objects.annotate(search = vector).filter(search = query)
        # memoires = memoire.objects.annotate(rank = SearchRank(vector, query)).filter(rank__gte = 0.3).order_by('-rank')
        memoires = memoire.objects.annotate(similarity=Greatest(
                                                            TrigramSimilarity('titre', search),
                                                            TrigramSimilarity('etudiant__nom', search),
                                                            TrigramSimilarity('etudiant__prenom', search),
                                                            TrigramSimilarity('resume', search),
                                                            # TrigramSimilarity('mot_cle', search),
                                                            # TrigramSimilarity('etudiant__enseignant__nom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__encadreur__nom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__encadreur__prenom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__president__nom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__examinateur__nom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__president__prenom_ens', search),
                                                            TrigramSimilarity('soutenance__jury__examinateur__prenom_ens', search),
                                                            TrigramSimilarity('etudiant__stage__entreprise__nom_ent', search),
                                                            TrigramSimilarity('etudiant__parcours__parcours', search),
                                                            )).filter(similarity__gte= 0.3).order_by('-similarity')

        # memoires = memoire.objects.filter(Q(titre__icontains = search)|
        #                                   Q(mot_cle__icontains = search)|
        #                                   Q(annee_academique__icontains = search)|
        #                                   Q(resume__icontains = search)|
        #                                   Q(etudiant__nom__icontains = search))
        # memoires =  memoire.objects.filter(Q(titre__search=search)|
        #                                    Q(mot_cle__search = search)|                                        
        #                                    Q(resume__search = search)|                                        
        #                                    Q(etudiant__prenom__search = search)|                                        
        #                                    Q(etudiant__nom__search = search))
        results_number = memoires.count()
        message = f'{results_number} resultats :'
        if results_number <= 1:
            message = f'{results_number} resultat :'
        context = {
            'memoires':memoires,
            'message':message,
        }
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'recherche.html')
def filtre(request):
    f = memoireFilter(request.GET, queryset=memoire.objects.all())
    context={
        'filter':f,
    }
    return render(request, 'consulter.html', context)
    # test1 = memoire.objects.all()
    # data = []
    # for mem in test1:
    #     data.append({
    #         'id':mem.id,
    #         'titre':mem.titre,
    #         'mot_cle':mem.mot_cle,
    #         'anne_academique':mem.annee_academique,
    #         'etudiant':mem.etudiant.nom,
    #         'parcours':mem.etudiant.parcours.parcours,
    #     })
    # # paginator = Paginator(data,6)
    # # page_number = request.GET.get('page')
    # # page_object = paginator.get_page(page_number)
    # # context = {'data':data,'memoires':page_object}
    # # mem = list(memoire.objects.values())
    # return JsonResponse(data, safe=False,)
def get_filtre(request, *args, **kwargs):
    selected_filtre= kwargs.get('filtre')
    test1 = memoire.objects.filter(etudiant__stage__entreprise__nom_ent__search =selected_filtre)
    data = []
    for mem in test1:
        data.append({
            'titre':mem.titre,
            'mot_cle':mem.mot_cle,
            'anne_academique':mem.annee_academique,
            'etudiant':mem.etudiant.nom,
            'parcours':mem.etudiant.parcours.parcours,
        })
    # etudiant_t = etudiant.objects.filter(pk =test1.etudiant_id)
    # test1.etudiant_id = etudiant_t
    # test = test1.values()
    # memoire_filtre = list(test)
    # etudiant_filtre = list(etudiant.objects.order_by('id').values())
    return JsonResponse(data, safe=False)