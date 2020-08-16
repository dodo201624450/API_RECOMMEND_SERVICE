from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import ApatemrForm
from .models import Aptamer


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
    if request.method == 'POST':
        form = ApatemrForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('aptamer:success')
    else:
        form = ApatemrForm()
    return render(request, 'aptamer/recommend_upload.html', {
        'form': form
    })
