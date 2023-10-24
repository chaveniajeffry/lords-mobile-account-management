from django.urls import path

from lm_accounts import views

urlpatterns = [
    path("", views.home, name="home-accounts"),
    path("create-lm-account/", views.createAccount, name="create-lm-account"),
    # path("admin/", admin.site.urls),
    
]