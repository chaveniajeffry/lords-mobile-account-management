from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-accounts"),
    # path("admin/", admin.site.urls),
    
]