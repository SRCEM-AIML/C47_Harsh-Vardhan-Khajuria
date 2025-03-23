from django.shortcuts import render

def app2_sample(request):
    return render(request, 'sample2.html')