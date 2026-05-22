from django import forms
from .models import Adherent


class AdherentForm(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = [
            'noms', 'prenoms', 'date_naissance', 'lieu_naissance',
            'nip', 'profession', 'lieu_residence', 'qualite',
            'province', 'commune', 'arrondissement', 'centre_vote',
            'telephone', 'adresse', 'email', 'photo', 'date_adhesion',
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'date_adhesion':  forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Champs obligatoires
        obligatoires = ['noms', 'prenoms', 'photo', 'nip', 'telephone']
        for champ in obligatoires:
            self.fields[champ].required = True

        # Champs optionnels
        optionnels = [
            'date_naissance', 'lieu_naissance', 'profession',
            'lieu_residence', 'qualite', 'province', 'commune',
            'arrondissement', 'centre_vote', 'adresse', 'email', 'date_adhesion'
        ]
        for champ in optionnels:
            self.fields[champ].required = False