from django.contrib import admin
from lm_accounts.models import LMUserAccount,LMUserBag,LMUserBagChest,LMUserBagCombat,LMUserBagResources,LMUserBagSpeedUp,LMUserBagUnique
# Register your models here.
admin.site.register(LMUserAccount)
admin.site.register(LMUserBag)
admin.site.register(LMUserBagChest)
admin.site.register(LMUserBagCombat)
admin.site.register(LMUserBagResources)
admin.site.register(LMUserBagSpeedUp)
admin.site.register(LMUserBagUnique)