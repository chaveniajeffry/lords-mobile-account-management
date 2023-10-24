from django import forms
from django.forms import ModelForm
from lm_accounts.models import LMUserAccount

class LMUserAccountForm(ModelForm):
    
    class Meta:
        model = LMUserAccount
        fields = [
            'IGN', 'reset_time', 'email', 'provider'
        ]