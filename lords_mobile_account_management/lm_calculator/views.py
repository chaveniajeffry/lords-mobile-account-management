from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home_message":"calculator page",
    }
    return render(request,'lm_calculator/home.html',context)