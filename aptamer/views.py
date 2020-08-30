import csv

from django.views import generic

from .forms import ApatmerForm

from feature_processing import preprocess_and_savez_protein
from hyperparams import *
from recommend_test import recommend100

from django.shortcuts import render, redirect

from .models import Aptamer


def file_list(request):
    imsi=[]
    aptamer = Aptamer.objects.latest('pk')
    f = open("media/data/RECOMMEND.csv", 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for i in rdr:
        imsi.append(i)
    print(imsi)
    nums = []
    for x in range(1, len(imsi)+1):
        x=str(x)
        nums.append(x)
    print(nums)
    e = enumerate(imsi)
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
            recommend100(imsi)
            aptamer.recommend = PAIRS_PATH["RECOMMEND"]
            aptamer.recommend_file = PAIRS_PATH["result"]
            aptamer.save()
            return redirect('aptamer:success')
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload.html', {
        'form': form,
    })


def load(request):
    return render(request, 'aptamer/recommend_success.html', {
    })


def upload_file2(request):
    imsi = []
    recommendFile = "/data/RECOMMEND.csv"
    if request.method == 'POST':
        form = ProteinForm(request.POST)
        if form.is_valid():
            aptamer = form.cleaned_data
            protein = aptamer.get('protein')
            preprocess_and_savez_protein(protein)
            recommend100(imsi)
            aptamer = recommend100(imsi)
            print(recommendFile)
            return render(request, 'aptamer/recommend_upload2.html', {
                'form': form,
                'recommendFile': recommendFile,
                'protein': protein,
                'aptamer': aptamer,
            })
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload2.html', {
        'form': form,
        'recommendFile': recommendFile,
    })


class LoadView(generic.DetailView):
    template_name = 'aptamer/loading_page.html'

    def get(request):
        imsi = []
        aptamer = Aptamer.objects.latest('protein')
        protein = aptamer.protein
        print(protein)
        print(type(protein))
        preprocess_and_savez_protein(protein)
        recommend100(imsi)
        recommendFile = PAIRS_PATH["result"]
        print(recommendFile)
        return render(request, 'aptamer/recommend_success.html', {
            'protein': protein,
            'recommendFile': recommendFile,
        })
        return render(request, 'aptamer/recommend_success.html', {
            'protein': protein,
            'recommendFile': recommendFile,
        })
