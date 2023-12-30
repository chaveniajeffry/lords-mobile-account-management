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
    path("create-research/", lm_research.createResearch, name="create-research"),
    path("update-research/<str:type>/<str:pk>/", lm_research.updateResearch, name="update-research"),
    path("delete-research/<str:type>/<str:pk>/", lm_research.deleteResearch, name="delete-research"),
]