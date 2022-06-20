from django.urls import path
from . import views

urlpatterns =[
    path('', views.home),
    path("legacy/", views.legacy, name="legacy"),
    path("version2/", views.version2, name="version2")
]