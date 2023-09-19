from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "home_message":"core page",
    }
    return render(request,'lm_core/home.html',context)