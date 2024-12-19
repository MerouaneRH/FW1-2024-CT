

from uo import views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about'),
    path('formation/<int:n>/', views.formation_detail, name='formation_detail'),

]