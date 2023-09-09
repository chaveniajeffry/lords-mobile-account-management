from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home_message":"infobank page",
    }
    return render(request,'lm_infobank/home.html',context)