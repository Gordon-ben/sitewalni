from django.urls import path
from . import views

urlpatterns = [
    path('',              views.index,          name='index'),
    path('formulaire/',   views.formulaire,     name='formulaire'),
    path('admin-login/',  views.admin_login,    name='admin_login'),
    path('dashboard/',    views.dashboard,      name='dashboard'),
    path('logout/',       views.admin_logout,   name='admin_logout'),
    path('fiche/<int:pk>/', views.fiche_detail, name='fiche_detail'),
    path('supprimer/<int:pk>/', views.supprimer_adherent, name='supprimer'),
]