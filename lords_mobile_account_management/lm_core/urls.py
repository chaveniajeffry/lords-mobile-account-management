from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-core"),
    # path("admin/", admin.site.urls),
    
]