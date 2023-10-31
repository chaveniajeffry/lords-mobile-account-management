from django import forms
from django.forms import ModelForm
from lm_accounts.models import LMUserAccount, LMUserBagChest

class LMUserAccountForm(ModelForm):
    
    class Meta:
        model = LMUserAccount
        fields = [
            'IGN', 'reset_time', 'email', 'provider'
        ]

class LMUserBagChestForm(ModelForm):
    
    class Meta:
        model = LMUserBagChest
        fields = [
            'name', 'count', 'bag_id'
        ]