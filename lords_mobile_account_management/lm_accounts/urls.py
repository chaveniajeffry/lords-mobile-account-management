from django.urls import path

from lm_accounts import views
from lm_accounts import lm_bag, lm_research

urlpatterns = [
    path("", views.home, name="home-accounts"),
    path("create-lm-account/", views.createAccount, name="create-lm-account"),
    path("read-lm-account/:<str:pk>/", views.readAccount, name="read-lm-account"),
    path("update-lm-account/:<str:pk>/", views.updateAccount, name="update-lm-account"),
    path("delete-lm-account/:<str:pk>/", views.deleteAcoount, name="delete-lm-account"),
    path("create-bag-chest/", lm_bag.createBagChest, name="create-bag-chest"),
    path("update-bag-chest/:<str:pk>/", lm_bag.updateBagChest, name="update-bag-chest"),
    path("delete-bag-chest/:<str:pk>/", lm_bag.deleteBagChest, name="delete-bag-chest"),
    path("create-bag-unique/", lm_bag.createBagUnique, name="create-bag-unique"),
    path("update-bag-unique/:<str:pk>/", lm_bag.updateBagUnique, name="update-bag-unique"),
    path("delete-bag-unique/:<str:pk>/", lm_bag.deleteBagUnique, name="delete-bag-unique"),
    path("create-bag-speed-up/", lm_bag.createBagSpeedUp, name="create-bag-speed-up"),
    path("update-bag-speed-up/:<str:pk>/", lm_bag.updateBagSpeedUp, name="update-bag-speed-up"),
    path("delete-bag-speed-up/:<str:pk>/", lm_bag.deleteBagSpeedUp, name="delete-bag-speed-up"),
    path("create-bag-combat/", lm_bag.createBagCombat, name="create-bag-combat"),
    path("update-bag-combat/:<str:pk>/", lm_bag.updateBagCombat, name="update-bag-combat"),
    path("delete-bag-combat/:<str:pk>/", lm_bag.deleteBagCombat, name="delete-bag-combat"),
    path("create-bag-resources/", lm_bag.createBagResources, name="create-bag-resources"),
    path("update-bag-resources/:<str:pk>/", lm_bag.updateBagResources, name="update-bag-resources"),
    path("delete-bag-resources/:<str:pk>/", lm_bag.deleteBagResources, name="delete-bag-resources"),
    path("create-research-economy/", lm_research.createResearchEconomy, name="create-research-economy"),
    path("update-research-economy/:<str:pk>/", lm_research.updateResearchEconomy, name="update-research-economy"),
    path("delete-research-economy/:<str:pk>/", lm_research.deleteResearchEconomy, name="delete-research-economy"),
]