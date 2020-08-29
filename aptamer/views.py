
from .forms import ApatmerForm, ProteinForm
from .models import Aptamer

from feature_processing import preprocess_and_savez_protein
from hyperparams import *
from recommend_test import recommend100

from django.shortcuts import render

def upload_file2(request):
    imsi = []
    cache_key = 'protein'
    recommendFile = "/data/RECOMMEND.csv"
    if request.method == 'POST':
        form = ProteinForm(request.POST)
        if form.is_valid():
            aptamer = form.cleaned_data
            protein = aptamer.get('protein')
            preprocess_and_savez_protein(protein)
            recommend100(imsi)
            print(recommendFile)
            return render(request, 'aptamer/recommend_upload2.html', {
                'form': form,
                'recommendFile': recommendFile,
                'protein': protein,
            })
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload2.html', {
        'form': form,
        'recommendFile': recommendFile,
    })
