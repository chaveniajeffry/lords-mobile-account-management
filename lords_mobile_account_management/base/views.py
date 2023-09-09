from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home_message":"home page",
    }
    return render(request,'base/home.html',context)