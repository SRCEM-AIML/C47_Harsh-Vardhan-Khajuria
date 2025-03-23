from django.contrib import admin
from django.urls import path
from dashboard import views
urlpatterns = [
path('',views.traffic_dashboard, name='dashboard'),
# path("about/", views.about, name="about")
]