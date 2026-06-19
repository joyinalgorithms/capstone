from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "reader/index.html")

def discover(request):
    return render(request, "reader/discover.html")

def mylibrary(request):
    return render(request, "reader/mylibrary.html")

def readinglists(request):
    return render(request, "reader/readinglists.html")

def savedquote(request):
    return render(request, "reader/savedquote.html")

def profile(request):
    return render(request, "reader/profile.html")

def settings(request):
    return render(request, "reader/settings.html")


    