from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Adherent
from .forms import AdherentForm


def index(request):
    return render(request, 'index.html')


def formulaire(request):
    if request.method == 'POST':
        form = AdherentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre fiche a été soumise avec succès !')
            return redirect('formulaire')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = AdherentForm()
    return render(request, 'formulaire.html', {'form': form})


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Identifiants incorrects.')
    return render(request, 'admin_login.html')


@login_required
def dashboard(request):
    q = request.GET.get('q', '')
    adherents = Adherent.objects.all()
    if q:
        adherents = adherents.filter(
            noms__icontains=q
        ) | adherents.filter(
            prenoms__icontains=q
        ) | adherents.filter(
            telephone__icontains=q
        ) | adherents.filter(
            province__icontains=q
        )

    now = timezone.now()
    total        = Adherent.objects.count()
    ce_mois      = Adherent.objects.filter(
        date_enregistrement__month=now.month,
        date_enregistrement__year=now.year
    ).count()
    provinces    = Adherent.objects.values('province').distinct().count()

    context = {
        'adherents': adherents,
        'all_adherents': Adherent.objects.all(),
        'total': total,
        'ce_mois': ce_mois,
        'provinces': provinces,
        'q': q,
    }
    return render(request, 'dashboard.html', context)


@login_required
def fiche_detail(request, pk):
    adherent = get_object_or_404(Adherent, pk=pk)
    return render(request, 'fiche_detail.html', {'a': adherent})


@login_required
def supprimer_adherent(request, pk):
    adherent = get_object_or_404(Adherent, pk=pk)
    if request.method == 'POST':
        adherent.delete()
        messages.success(request, 'Adhérent supprimé avec succès.')
        return redirect('dashboard')
    return render(request, 'confirmer_suppression.html', {'a': adherent})


def admin_logout(request):
    logout(request)
    return redirect('admin_login')