from django.urls import path
from .views import homePage_view, aboutPage_view

urlpatterns = [
      path("about/", aboutPage_view),
      path("", homePage_view),
]