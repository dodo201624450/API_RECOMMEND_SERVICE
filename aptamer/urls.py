from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

from. import views

app_name = 'aptamer'

urlpatterns = [
    path('recommend/', views.upload, name='index'),
    path('recommend/success', views.file_list, name='success'),
    path('recommend/upload', views.upload_file, name='upload'),
    path('recommend/success2', views.file_list, name='success2'),
    path('recommend/upload2', views.upload_file, name='upload2'),
    path('recommend/ex', views.index, name='ex'),
]