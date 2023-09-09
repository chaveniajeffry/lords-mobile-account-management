from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-calculator"),
    # path("admin/", admin.site.urls),
    
]