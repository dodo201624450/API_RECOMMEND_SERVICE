from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

from. import views

app_name = 'aptamer'

urlpatterns = [
    path('recommend/upload2', views.upload_file2, name='upload'),
]