from django.shortcuts import render,get_object_or_404
from .models import Formation


# Create your views here.


def about(request):
    return render(request,"uo/about.html")


def formation_detail(request, n):
    formation = get_object_or_404(Formation, pk=n)
    ues = formation.ue_set.all()  

    return render(request, 'uo/formation_detail.html', {'formation': formation, 'ues': ues})
