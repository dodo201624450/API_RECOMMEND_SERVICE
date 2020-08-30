from django.urls import path

from. import views

app_name = 'aptamer'

urlpatterns = [
    path('recommend/success', views.file_list, name='success'),
    path('recommend/upload', views.upload_file, name='upload'),
]