from django.shortcuts import render,get_object_or_404, redirect
from .models import Formation,UE
from .forms import UEForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User 


# Create your views here.


def about(request):
    return render(request,"uo/about.html")

def home(request):
    return render(request, 'uo/home.html')

def formation_detail(request, n):
    formation = get_object_or_404(Formation, pk=n)
    ues = formation.ue_set.all()  

    return render(request, 'uo/formation_detail.html', {'formation': formation, 'ues': ues})

def ue_detail(request, m):
    ue = get_object_or_404(UE, id=m)
    formations = ue.formations.all()

    return render(request, 'uo/ue_detail.html', {'ue': ue, 'formations': formations})

def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'uo/formation_list.html', {'formations': formations})

def ue_list(request):
    ues = UE.objects.all()
    return render(request, 'uo/ue_list.html', {'ues': ues})

@login_required
def ue_add(request):
    # Vérifiez les formations pour lesquelles l'utilisateur est responsable
    formations_responsable = Formation.objects.filter(responsable=request.user)

    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            ue = form.save()
            return redirect('ue_list')
    else:
        form = UEForm()

    return render(request, 'uo/ue_add.html', {
        'form': form,
        'formations_responsable': formations_responsable
    })

@login_required
def ue_edit(request, m):
    ue = get_object_or_404(UE, id=m)

    if request.method == 'POST':
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            return redirect(f'/ue/{ue.id}/') 
    else:
        form = UEForm(instance=ue)

    return render(request, 'uo/ue_edit.html', {'form': form, 'ue': ue})

from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def ue_delete(request, m):
    ue = get_object_or_404(UE, id=m)

    if request.method == 'POST':
        ue.delete()
        return HttpResponseRedirect(reverse('ue_list'))  # Redirige vers la liste des UE après suppression

    return render(request, 'uo/ue_delete.html', {'ue': ue})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect('home')  # Rediriger vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'uo/login.html')

def custom_logout(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect('home')  # Rediriger vers la page d'accueil

@login_required
def formation_stats(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)

    # Vérifie si l'utilisateur est responsable de la formation
    if formation.responsable != request.user:
        raise PermissionDenied("Accès refusé : vous n'êtes pas responsable de cette formation.")

    # Calcul des statistiques
    ues = formation.ue_set.all()  # Obtenir toutes les UE liées à la formation
    nombre_ues = ues.count()
    print("avant le tri")
    # Obtenir tous les responsables des UE liés à la formation, triés par ordre alphabétique
    responsables_ue = (
        User.objects.filter(ue__in=ues)  # Filtrer les utilisateurs responsables des UE
        .distinct()
        .order_by("last_name", "first_name")  # Trier par ordre alphabétique
    )
    print("après le tri"+str(responsables_ue))
    volume_cm = sum(ue.CM for ue in ues)
    volume_td = sum(ue.TD for ue in ues)
    volume_tp = sum(ue.TP for ue in ues)
    volume_total_equivalent_td = volume_cm * 1.5 + volume_td + volume_tp
    total_ects = sum(ue.credits for ue in ues)

    # Envoie des données au template
    context = {
        'formation': formation,
        'nombre_ues': nombre_ues,
        'responsables_ue': responsables_ue,
        'volume_cm': volume_cm,
        'volume_td': volume_td,
        'volume_tp': volume_tp,
        'volume_total_equivalent_td': volume_total_equivalent_td,
        'total_ects': total_ects,
    }
    return render(request, 'uo/formation_stats.html', context)