from django.urls import path

from. import views

app_name = 'aptamer'
urlpatterns = [
    path('recommend/', views.IndexView.as_view(), name='index'),
    path('recommend/success/', views.IndexView.as_view(), name='success'),
]