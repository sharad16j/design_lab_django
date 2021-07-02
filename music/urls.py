from django.contrib import admin
from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('',views.musicweb,name='homepage'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('musicweb1/',views.musicweb1,name='homepage1'),
    path('musicweb2/',views.musicweb2,name='homepage2'),
    path('musicweb3/',views.musicweb3,name='homepage3'),
    path('musicweb4/',views.musicweb4,name='homepage4'),
    path('musicweb5/',views.musicweb5,name='homepage5'),
    path('login', views.login_function, name='login'),
    path('signup', views.signup, name='signup'),
    path('formpage', views.formpage, name='formpage'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add',views.songpost,name='advertise'),
    path('ajax/', views.ajax_view, name="ajax"),


]

