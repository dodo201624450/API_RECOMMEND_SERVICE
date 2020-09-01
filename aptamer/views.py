import csv
import re

from .forms import ApatmerForm

from feature_processing import preprocess_and_savez_protein
from hyperparams import *
from recommend_test import recommend100

from django.shortcuts import render, redirect

from .models import Aptamer


def file_list(request):
    imsi=[]
    aptamer = Aptamer.objects.latest('pk')
    f = open("media/data/RECOMMEND.csv", 'r')
    rdr = csv.reader(f)
    for i in rdr:
        imsi.append(i)
    print(imsi)
    nums = []
    for x in range(1, len(imsi)+1):
        x = str(x)
        nums.append(x)
    print(nums)
    e = enumerate(imsi, start=1)
    return render(request, 'aptamer/recommend_success.html', {
        'aptamer': aptamer,
        'e': e,
    })


def upload_file(request):
    imsi=[]
    if request.method == 'POST':
        form = ApatmerForm(request.POST)
        if form.is_valid():
            aptamer = form.save(commit=False)
            protein = aptamer.protein
            preprocess_and_savez_protein(protein)
            aptamer.number_of_actual, aptamer.number_of_all = recommend100(imsi, (int)(aptamer.number_of_recommended))
            aptamer.recommend_file = PAIRS_PATH["result"]
            aptamer.all_file = PAIRS_PATH["all"]
            aptamer.save()
            return redirect('aptamer:success')
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload.html', {
        'form': form,
    })
