from django import forms
from .models import Aptamer
from django.utils.translation import gettext_lazy as _

class ApatmerForm(forms.ModelForm):
    class Meta:
        model = Aptamer
        fields = ['protein','number_of_recommended']
        labels={
            'protein': _('Target Protein'),
            'number_of_recommended': _('최대 추천 수'),
        }

