from django.urls import path

from. import views

app_name = 'home'
urlpatterns = [
    path('ex/', views.IndexView.as_view(), name='index'),
    path('', views.Index2View.as_view(), name='index2'),
]