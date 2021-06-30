from django import forms

from installation.models import Direction, Installation
from .models import Equipement, Category


class EquipementForm(forms.ModelForm):

    class Meta:
        model = Equipement
        fields = ['num_serie','nom','category']

    def clean_num_serie(self):
        cd = self.cleaned_data
        if(Equipement.objects.filter(num_serie=cd['num_serie']).exists()):
            raise forms.ValidationError(f"Numero Serie { cd['num_serie']}  existe deja ")
        return cd['num_serie']



class EquipementFormm(forms.ModelForm):

    class Meta:
        model = Equipement
        fields = ['num_serie','nom','category']






class AtributForm(forms.ModelForm):

    class Meta:
        model = Equipement
        fields = ['etat_equipement']

#datil equipement deja installer
class EquipInstall(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ['ip', 'mac','Nom_direction']

    def clean_ip(self):
        cd = self.cleaned_data
        if (Installation.objects.filter(ip=cd['ip']).exists()):
            raise forms.ValidationError(f" Ip {cd['ip']}   deja existe ")
        return cd['ip']


    def clean_mac(self):
        cd = self.cleaned_data
        if (Installation.objects.filter(mac=cd['mac']).exists()):
            raise forms.ValidationError(f" Adresse mac {cd['mac']}   deja existe ")
        return cd['mac']


#form add_categorie_equipement
class CategorieForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name',]

    def clean_name(self):
        cd = self.cleaned_data
        if (Category.objects.filter(name=cd['name']).exists()):
            raise forms.ValidationError(f"La categorie { cd['name']}   deja existe ")
        return cd['name']


#form add_direction
class DirectionForm(forms.ModelForm):

    class Meta:
        model = Direction
        fields = ['Nom']

    def clean_Nom(self):
        cd = self.cleaned_data
        if (Direction.objects.filter(Nom=cd['Nom']).exists()):
            raise forms.ValidationError(f"Cet nom direction  {cd['Nom']} deja existe ")
        return cd['Nom']






