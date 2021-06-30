from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone



# Create your models here.


EQUIPEMENT_ETAT=(
    ('0','Non attribut'),
    ('1','Attribué'),
)

class Equipement(models.Model):
    num_serie=models.CharField(max_length=20)
    nom=models.CharField(max_length=20)
    date_ajoute=models.DateTimeField(default=timezone.now)
    etat_equipement = models.CharField(max_length=15, choices=EQUIPEMENT_ETAT,default='0',verbose_name='etat')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categoryE')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('equip:detail_equipement', args=[self.pk])
        # return reverse('equip:add_equipement')


    def __str__(self):
        return self.num_serie





class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nom Du Categorie")

    def __str__(self):
        return self.name





