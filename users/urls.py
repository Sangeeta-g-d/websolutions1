from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [

    path("index",views.index,name='index'),
    path("ad_login",views.ad_login,name='ad_login'),
    path("admin_db",views.admin_db,name='admin_db'),
    path("admin_logout",views.admin_logout,name='admin_logout'),

    ]
