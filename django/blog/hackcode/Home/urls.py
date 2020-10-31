
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="Home"),

    path('about/',views.about,name="about"),
    
    path('contact/',views.Contact,name="contact"),

    path('search/', views.search,name="search"),

    path('signup', views.handleSignUp,name="handleSignUp"),

    path('login', views.handleLogIn,name="handleLogIn"),
    

   path('logout/', views.handleLogOut,name="handleLogOut"),
   
]
