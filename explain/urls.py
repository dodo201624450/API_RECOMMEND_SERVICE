from django.urls import path

from. import views

app_name = 'explain'
urlpatterns = [
    path('project/', views.ProjectView.as_view(), name='project'),
    path('requirement/', views.RequirementView.as_view(), name='requirement'),
    path('measures/', views.MeasuresView.as_view(), name='measures'),
    path('team/', views.TeamView.as_view(), name='team'),
]