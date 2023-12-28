from django.urls import path

from lm_accounts import views
from lm_accounts import lm_bag, lm_research

urlpatterns = [
    path("", views.home, name="home-accounts"),
    path("create-lm-account/", views.createAccount, name="create-lm-account"),
    path("read-lm-account/:<str:pk>/", views.readAccount, name="read-lm-account"),
    path("update-lm-account/:<str:pk>/", views.updateAccount, name="update-lm-account"),
    path("delete-lm-account/:<str:pk>/", views.deleteAcoount, name="delete-lm-account"),
    path("create-bag/", lm_bag.createBag, name="create-bag"),
    path("update-bag/<str:type>/<str:pk>/", lm_bag.updateBag, name="update-bag"),
    path("delete-bag/<str:type>/<str:pk>/", lm_bag.deleteBag, name="delete-bag"),
    path("create-research-economy/", lm_research.createResearchEconomy, name="create-research-economy"),
    path("update-research-economy/:<str:pk>/", lm_research.updateResearchEconomy, name="update-research-economy"),
    path("delete-research-economy/:<str:pk>/", lm_research.deleteResearchEconomy, name="delete-research-economy"),
    path("create-research-defense/", lm_research.createResearchDefense, name="create-research-defense"),
    path("update-research-defense/:<str:pk>/", lm_research.updateResearchDefense, name="update-research-defense"),
    path("delete-research-defense/:<str:pk>/", lm_research.deleteResearchDefense, name="delete-research-defense"),
    path("create-research-military/", lm_research.createResearchMilitary, name="create-research-military"),
    path("update-research-military/:<str:pk>/", lm_research.updateResearchMilitary, name="update-research-military"),
    path("delete-research-military/:<str:pk>/", lm_research.deleteResearchMilitary, name="delete-research-military"),
    path("create-research-monster-hunt/", lm_research.createResearchMonsterHunt, name="create-research-monster-hunt"),
    path("update-research-monster-hunt/:<str:pk>/", lm_research.updateResearchMonsterHunt, name="update-research-monster-hunt"),
    path("delete-research-monster-hunt/:<str:pk>/", lm_research.deleteResearchMonsterHunt, name="delete-research-monster-hunt"),
    path("create-research-upgrade-defenses/", lm_research.createResearchUpgradeDefenses, name="create-research-upgrade-defenses"),
    path("update-research-upgrade-defenses/:<str:pk>/", lm_research.updateResearchUpgradeDefenses, name="update-research-upgrade-defenses"),
    path("delete-research-upgrade-defenses/:<str:pk>/", lm_research.deleteResearchUpgradeDefenses, name="delete-research-upgrade-defenses"),
]