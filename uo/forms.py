from django import forms
from .models import UE

class UEForm(forms.ModelForm):
    class Meta:
        model = UE
        fields = ['titre', 'description', 'CM', 'TD', 'TP', 'credits', 'responsables', 'formations']
        widgets = {
            'responsables': forms.CheckboxSelectMultiple(),
            'formations': forms.CheckboxSelectMultiple(),
        }