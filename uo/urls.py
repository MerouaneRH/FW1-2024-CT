

from uo import views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about'),
    path('formation/<int:n>/', views.formation_detail, name='formation_detail'),
    path('ue/<int:m>/', views.ue_detail, name='ue_detail'),
    path('formations/', views.formation_list, name='formation_list'),


]