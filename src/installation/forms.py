from django import forms
from django.forms import DateInput

from .models import Installation

class DateInput(forms.DateInput):
    input_type = 'date'

class InstallationForm(forms.ModelForm):

    class Meta:
        model = Installation
        fields = ['ip','mac','Nom_direction','date_update']
        widgets = {
            'date_update': DateInput()
        }

    def clean_ip(self):
        cd = self.cleaned_data
        if (Installation.objects.filter(ip=cd['ip']).exists()):
            raise forms.ValidationError(f" Ip { cd['ip']}   deja existe ")
        return cd['ip']

    def clean_mac(self):
        cd = self.cleaned_data
        if (Installation.objects.filter(mac=cd['mac']).exists()):
            raise forms.ValidationError(f" Adresse mac {cd['mac']}   deja existe ")
        return cd['mac']





class InstallationFormm(forms.ModelForm):
    date_installe = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = Installation
        fields = ['ip','mac','Nom_direction']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ['service',]