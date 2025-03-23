from django.shortcuts import render,HttpResponse


# Create your views here.
def traffic_dashboard(request):
    return render(request,'dashboard.html')

# def about(request):
#     return HttpResponse("This is about page")