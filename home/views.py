from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template


class IndexView(generic.DetailView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)

