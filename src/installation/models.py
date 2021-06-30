from django.contrib.auth.models import User
from django.db import models

from equipement.models import Equipement
from macaddress.fields import MACAddressField
# Create your models here.
from django.utils import timezone


SERVICE_ETAT=(
    ('En service','En service'),
    ('En panne','En panne'),

)


class Installation(models.Model):
    ip=models.GenericIPAddressField(max_length=20)
    mac=MACAddressField(verbose_name='Adesse Mac')
    date_installe=models.DateTimeField(default=timezone.now)
    date_update=models.DateTimeField(null=True)
    Nom_direction = models.ForeignKey('Direction', on_delete=models.CASCADE, related_name='nomD')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    equipement_installe = models.OneToOneField(Equipement, on_delete=models.CASCADE, related_name='installation_equipement')
    service = models.CharField(max_length=15, choices=SERVICE_ETAT, default='En service')


    def __str__(self):
        return 'Ip: {} - Mac: {}'.format(self.ip, self.mac)




class Direction(models.Model):
    Nom = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.Nom)

