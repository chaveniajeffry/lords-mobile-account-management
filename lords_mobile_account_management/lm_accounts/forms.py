from django import forms
from django.forms import ModelForm
from lm_accounts.models import *

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

class LMUserBagUniqueForm(ModelForm):
    
    class Meta:
        model = LMUserBagUnique
        fields = [
            'name', 'count', 'bag_id'
        ]

class LMUserBagSpeedUpForm(ModelForm):
    
    class Meta:
        model = LMUserBagSpeedUp
        fields = [
            'name', 'count', 'bag_id'
        ]
 
class LMUserBagCombatForm(ModelForm):
    
    class Meta:
        model = LMUserBagCombat
        fields = [
            'name', 'count', 'bag_id'
        ]
        
class LMUserBagResourcesForm(ModelForm):
    
    class Meta:
        model = LMUserBagResources
        fields = [
            'name', 'count', 'bag_id'
        ]

class LMUserResearchEconomyForm(ModelForm):
    
    class Meta:
        model = LMUserResearchEconomy
        fields = [
            'name', 'level', 'research'
        ]

class LMUserResearchDefenseForm(ModelForm):
    
    class Meta:
        model = LMUserResearchDefense
        fields = [
            'name', 'level', 'research'
        ]
        
class LMUserResearchMilitaryForm(ModelForm):
    
    class Meta:
        model = LMUserResearchMilitary
        fields = [
            'name', 'level', 'research'
        ]

class LMUserResearchMonsterHuntForm(ModelForm):
    
    class Meta:
        model = LMUserResearchMonsterHunt
        fields = [
            'name', 'level', 'research'
        ]
        
class LMUserResearchUpgradeDefensesForm(ModelForm):
    
    class Meta:
        model = LMUserResearchUpgradeDefenses
        fields = [
            'name', 'level', 'research'
        ]



class LMUserResearchUpgradeMilitaryForm(ModelForm):
    
    class Meta:
        model = LMUserResearchUpgradeMilitary
        fields = [
            'name', 'level', 'research'
        ]