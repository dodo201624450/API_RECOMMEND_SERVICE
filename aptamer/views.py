from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import ApatmerForm
from .models import Aptamer

from feature_processing import preprocess_and_savez_protein
from hyperparams import *
from recommend_test import recommend100


def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)

    return render(request, 'aptamer/recommend.html', context)


def file_list(request):
    aptamer = Aptamer.objects.all()
    return render(request, 'aptamer/recommend_success.html', {
        'aptamer':aptamer
    })


def upload_file(request):
    imsi = []
    if request.method == 'POST':
        form = ApatmerForm(request.POST)
        if form.is_valid():
            aptamer = form.save(commit=False)
            preprocess_and_savez_protein(aptamer.protein)
            recommend100(imsi)
            aptamer.recommend = PAIRS_PATH["RECOMMEND"]
            aptamer.recommend_file = PAIRS_PATH["result"]
            aptamer.save()
            return redirect('aptamer:success')
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload.html', {
        'form': form
    })
