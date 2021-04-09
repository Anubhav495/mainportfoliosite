from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")
def cp(request):
    return render(request,"Cp.html")
def ask(request):
    return render(request,"Ask.html")
def proj(request):
    return render(request,"Projects.html")
def about(request):
    return render(request,"About.html")

