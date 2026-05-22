from django.db import models

class Adherent(models.Model):
    # Identification civique
    noms             = models.CharField(max_length=100)
    prenoms          = models.CharField(max_length=100)
    date_naissance   = models.DateField(blank=True, null=True)
    lieu_naissance   = models.CharField(max_length=150, blank=True)
    nip              = models.CharField(max_length=50)
    profession       = models.CharField(max_length=150, blank=True)
    lieu_residence   = models.CharField(max_length=150, blank=True)
    qualite          = models.CharField(max_length=100, blank=True)

    # Localisation territoriale
    province         = models.CharField(max_length=100, blank=True)
    commune          = models.CharField(max_length=100, blank=True)
    arrondissement   = models.CharField(max_length=100, blank=True)
    centre_vote      = models.CharField(max_length=150, blank=True)

    # Contacts
    telephone        = models.CharField(max_length=30)
    adresse          = models.CharField(max_length=200, blank=True)
    email            = models.EmailField(blank=True)

    # Photo
    photo            = models.ImageField(upload_to='photos/', null=True)

    # Adhésion
    date_adhesion    = models.DateField(blank=True, null=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_enregistrement']
        verbose_name = 'Adhérent'
        verbose_name_plural = 'Adhérents'

    def __str__(self):
        return f"{self.prenoms} {self.noms}"