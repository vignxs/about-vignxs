from django.urls import path
from . import views

urlpatterns =[
    path('', views.home),
    path("legacy/", views.legacy, name="legacy"),
    path("version2/", views.version2, name="version2"),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]