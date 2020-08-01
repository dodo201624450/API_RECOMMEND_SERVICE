from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template


class ProjectView(generic.DetailView):
    template_name = 'explain/project.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class RequirementView(generic.DetailView):
    template_name = 'explain/requirement.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class MeasuresView(generic.DetailView):
    template_name = 'explain/measures.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class TeamView(generic.DetailView):
    template_name = 'explain/team.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)
