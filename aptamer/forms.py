from django import forms
from .models import Aptamer

class ApatmerForm(forms.ModelForm):
    class Meta:
        model = Aptamer
        fields = ('protein',)

