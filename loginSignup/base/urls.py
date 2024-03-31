from django.urls import path, include
from .views import authView, home

from . import views

app_name = 'base'

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path('logout/', views.logout_view, name='logout'),
]
