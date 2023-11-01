from django.urls import path

from lm_accounts import views

urlpatterns = [
    path("", views.home, name="home-accounts"),
    path("create-lm-account/", views.createAccount, name="create-lm-account"),
    path("read-lm-account/:<str:pk>/", views.readAccount, name="read-lm-account"),
    path("update-lm-account/:<str:pk>/", views.updateAccount, name="update-lm-account"),
    path("delete-lm-account/:<str:pk>/", views.deleteAcoount, name="delete-lm-account"),
    path("create-bag-chest/", views.createBagChest, name="create-bag-chest"),
    path("update-bag-chest/:<str:pk>/", views.updateBagChest, name="update-bag-chest"),
    path("delete-bag-chest/:<str:pk>/", views.deleteBagChest, name="delete-bag-chest"),
]