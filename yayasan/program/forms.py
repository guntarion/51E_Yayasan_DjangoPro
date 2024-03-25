# forms.py
from django import forms
from .models import ProgramKerja

class ProgramKerjaForm(forms.ModelForm):
    class Meta:
        model = ProgramKerja
        fields = '__all__'