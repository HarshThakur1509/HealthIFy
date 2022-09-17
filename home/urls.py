from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("doctor", views.doctor, name="doctor"),
    path('history', views.history, name='history'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signup, name="signup"),
]
