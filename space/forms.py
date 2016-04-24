from django import forms

from .models import Symptom

class SymptomForm(forms.ModelForm):

    class Meta:
        model = Symptom
        fields = ('symptomName', 'intensity', 'streetaddress', 'city', 'province', 'postal', 'country',)
    
class CityForm(forms.Form):
    city = forms.CharField(label="City", max_length=200, required=False)
    state = forms.CharField(label="State", max_length=200, required=False)