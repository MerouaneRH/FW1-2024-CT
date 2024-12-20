from django.shortcuts import render,get_object_or_404, redirect
from .models import Formation,UE
from .forms import UEForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def about(request):
    return render(request,"uo/about.html")


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

def ue_add(request):
    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ue_list')
    else:
        form = UEForm()
    return render(request, 'uo/ue_add.html', {'form': form})

def home(request):
    return render(request, 'uo/home.html')

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