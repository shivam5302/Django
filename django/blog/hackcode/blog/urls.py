
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('postComment',views.PostComment,name="PostCommant"),
    path('',views.blogHome,name="blogHome"),
    path('<str:slug>/',views.blogPost,name="blogPost"),
]
