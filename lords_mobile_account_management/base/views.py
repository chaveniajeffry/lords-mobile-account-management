from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def signin(request):
    return render(request, 'base/signin.html')

# logout user then return to sign in page
def signout(request):
    logout(request)
    return render(request, 'base/signin.html')
class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('login')

@login_required
def home(request):
    context = {
        "home_message":"home page",
    }
    return render(request,'base/home.html',context)