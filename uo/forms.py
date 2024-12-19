from django import forms
from .models import UE

class UEForm(forms.ModelForm):
    class Meta:
        model = UE
        fields = ['titre', 'description', 'CM', 'TD', 'TP', 'credits', 'responsables', 'formations']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'CM': forms.NumberInput(attrs={'class': 'form-control'}),
            'TD': forms.NumberInput(attrs={'class': 'form-control'}),
            'TP': forms.NumberInput(attrs={'class': 'form-control'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
            'responsables': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
            'formations': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }