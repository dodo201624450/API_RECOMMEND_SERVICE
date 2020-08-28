from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import ApatmerForm, ProteinForm
from .models import Aptamer

from feature_processing import preprocess_and_savez_protein
from hyperparams import *
from recommend_test import recommend100

from django.shortcuts import render
from .task import go_to_sleep


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

def apatmer_list(request):
    template_name = 'apatmer/recommend_success2.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


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
            return redirect('aptamer:success', aptamer='aptamer')
    else:
        form = ApatmerForm()
    return render(request, 'aptamer/recommend_upload.html', {
        'form': form
    })

def upload_file_no_model(request):
    form = ProteinForm()
    if request.method == 'POST':
        form = ProteinForm(request.POST)
        if form.is_vaild():
            _protein = form.cleaned_data
            protein = _protein.get('protein')

def index(request):
    task = go_to_sleep.delay(1)

    return render(request, 'aptamer/example.html', {'task_id':task.task_id})