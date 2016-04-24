from django import forms

from .models import Symptom

class SymptomForm(forms.ModelForm):

    class Meta:
        model = Symptom
        fields = ('symptom_name', 'intensity', 'street_address', 'city', 'province', 'postal', 'country',)