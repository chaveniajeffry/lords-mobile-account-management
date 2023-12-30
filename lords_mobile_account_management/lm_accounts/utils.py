from lm_accounts.models import *
from lm_accounts.forms import *

def checkModel(type=None, category=None) -> models:
    LM_CATEGORY = {'bag', 'research'}
    
    LM_MODEL = {
        'bag-chest': LMUserBagChest,
        'bag-unique': LMUserBagUnique,
        'bag-speed-up': LMUserBagSpeedUp,
        'bag-combat': LMUserBagCombat,
        'bag-resources': LMUserBagResources,

        'research-economy': LMUserResearchEconomy,
        'research-defense': LMUserResearchDefense,
        'research-military': LMUserResearchMilitary,
        'research-monster-hunt': LMUserResearchMonsterHunt,
        'research-upgrade-defenses': LMUserResearchUpgradeDefenses,
        'research-upgrade-military': LMUserResearchUpgradeMilitary,
        'research-army-leadership': LMUserResearchArmyLeadership,
        'research-military-command': LMUserResearchMilitaryCommand,
        'research-familiar': LMUserResearchFamiliar,
        'research-familiar-battles': LMUserResearchFamiliarBattles,
        'research-sigil': LMUserResearchSigil,
        'research-wonder-battles': LMUserResearchWonderBattles,
        'research-gear': LMUserResearchGear,
        'research-advanced-wonder-battles': LMUserResearchAdvancedWonderBattles,


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
        'bag-chest': LMUserBagChestForm,
        'bag-unique': LMUserBagUniqueForm,
        'bag-speed-up': LMUserBagSpeedUpForm,
        'bag-combat': LMUserBagCombatForm,
        'bag-resources': LMUserBagResourcesForm,

        'research-economy': LMUserResearchEconomyForm,
        'research-defense': LMUserResearchDefenseForm,
        'research-military': LMUserResearchMilitaryForm,
        'research-monster-hunt': LMUserResearchMonsterHuntForm,
        'research-upgrade-defenses': LMUserResearchUpgradeDefensesForm,
        'research-upgrade-military': LMUserResearchUpgradeMilitaryForm,
        'research-army-leadership': LMUserResearchArmyLeadershipForm,
        'research-military-command': LMUserResearchMilitaryCommandForm,
        'research-familiar': LMUserResearchFamiliarForm,
        'research-familiar-battles': LMUserResearchFamiliarBattlesForm,
        'research-sigil': LMUserResearchSigilForm,
        'research-wonder-battles': LMUserResearchWonderBattlesForm,
        'research-gear': LMUserResearchGearForm,
        'research-advanced-wonder-battles': LMUserResearchAdvancedWonderBattlesForm,
    }
    if category in LM_CATEGORY:
        if type in LM_MODEL:
            return LM_MODEL[type]
        else:
            return None
    else:
        return None
