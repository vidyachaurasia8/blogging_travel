from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("index/",views.index),
    path("aboutus/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("category/",views.category),
    path("services/",views.services),
    path("login/",views.login),
    path("register/",views.register),
    path("package/",views.package),
    path("logout/",views.logout),
    path("contact/",views.contact),
    
    
]