from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home_message":"accounts page",
    }
    return render(request,'lm_accounts/home.html',context)