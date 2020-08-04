from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template
from .forms import UploadFileForm


class IndexView(generic.DetailView):
    template_name = 'aptamer/recommend.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)

    def upload_File(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("{% url aptamer:success %}")
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
