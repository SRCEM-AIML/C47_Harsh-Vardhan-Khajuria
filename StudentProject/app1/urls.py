from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sample/', views.app1_sample, name='sample'),
]