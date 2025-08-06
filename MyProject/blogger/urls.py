from django.urls import path
from . import views

urlpatterns=[
    path("package/",views.index),
    path("dashboard/",views.dashboard),
    path("myblogs/",views.myblogs),
    path("history/",views.history),
    path("profile/",views.profile),
    path("logout/",views.signout),
]