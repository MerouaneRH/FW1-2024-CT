from uo import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('formation/<int:n>/', views.formation_detail, name='formation_detail'),
    path('ue/<int:m>/', views.ue_detail, name='ue_detail'),
    path('formations/', views.formation_list, name='formation_list'),
    path('ues/', views.ue_list, name='ue_list'),
    path('ue/ajouter/', views.ue_add, name='ue_add'),
    path('', views.home, name='home'),
    path('ue/modifier/<int:m>/', views.ue_edit, name='ue_edit'),
    path('ue/supprimer/<int:m>/', views.ue_delete, name='ue_delete'),
    
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),

    path("formation/<int:formation_id>/stats/", views.formation_stats, name="formation_stats"),



]