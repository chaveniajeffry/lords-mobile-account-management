from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-infobank"),
    # path("admin/", admin.site.urls),
    
]