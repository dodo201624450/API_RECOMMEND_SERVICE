from django import forms
from .models import Aptamer

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=15)
    files = forms.FileField()

class ApatemrForm(forms.ModelForm):
    class Meta:
        model = Aptamer
        fields = ('f_object',)