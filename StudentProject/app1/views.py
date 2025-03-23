from django.shortcuts import render

def homepage(request):
    return render(request, 'app1/homepage.html')

def app1_sample(request):
    return render(request, 'sample.html')