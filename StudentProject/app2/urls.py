
from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.app2_sample, name='app2_sample'),
]