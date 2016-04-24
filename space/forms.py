from django import forms

from .models import Symptom

class SymptomForm(forms.ModelForm):

    class Meta:
        model = Symptom
        fields = ('symptomName', 'intensity', 'streetaddress', 'city', 'province', 'postal', 'country',)