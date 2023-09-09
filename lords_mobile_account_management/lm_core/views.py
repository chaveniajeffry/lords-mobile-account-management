from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home_message":"core page",
    }
    return render(request,'lm_core/home.html',context)