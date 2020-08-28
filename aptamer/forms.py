from django import forms
from .models import Aptamer

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=15)
    files = forms.FileField()

class ApatmerForm(forms.ModelForm):
    class Meta:
        model = Aptamer
        fields = ('protein',)

class ProteinForm(forms.Form):
    protein = forms.CharField(max_length=2000)
