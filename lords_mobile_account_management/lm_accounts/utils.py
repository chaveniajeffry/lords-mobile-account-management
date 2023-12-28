from lm_accounts.models import *
from lm_accounts.forms import *

def checkModel(type=None, category=None) -> models:
    LM_CATEGORY = {'bag', 'research'}
    
    LM_MODEL = {
        'bag_chest': LMUserBagChest,
        'bag_unique': LMUserBagUnique,
        'bag_speed_up': LMUserBagSpeedUp,
        'bag_combat': LMUserBagCombat,
        'bag_resources': LMUserBagResources,
    }
    if category in LM_CATEGORY:
        if type in LM_MODEL:
            return LM_MODEL[type]
        else:
            return None
    else:
        return None

def checkForm(type=None, category=None) -> forms:
    LM_CATEGORY = {'bag', 'research'}
    
    LM_MODEL = {
        'bag_chest': LMUserBagChestForm,
        'bag_unique': LMUserBagUniqueForm,
        'bag_speed_up': LMUserBagSpeedUpForm,
        'bag_combat': LMUserBagCombatForm,
        'bag_resources': LMUserBagResourcesForm,
    }
    if category in LM_CATEGORY:
        if type in LM_MODEL:
            return LM_MODEL[type]
        else:
            return None
    else:
        return None
