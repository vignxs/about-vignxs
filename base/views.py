from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def legacy(request):
    return render(request, "legacy.html")
  
def version2(request):
    return render(request, "version2.html")

def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')
