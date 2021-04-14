from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")
def cp(request):
    return render(request,"Cp.html")
def contact(request):
    return render(request,"contact.html")
def proj(request):
    return render(request,"Projects.html")
def about(request):
    return render(request,"About.html")

