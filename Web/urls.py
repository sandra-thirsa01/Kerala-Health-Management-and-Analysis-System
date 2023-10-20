from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('login',views.loginaction),
    path('welcome',views.welcomeaction),
    path('child disease',views.childdisease),
    path('child vaccination',views.childvaccination)
]
