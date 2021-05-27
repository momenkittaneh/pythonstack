from django.urls import path
from . import views


urlpatterns = [

    path('',views.index),    #for the first page
    path('register',views.regis), #for the register 
    path('login',views.login), #for the login
    path('logout',views.logout), #for the logout
    path('welcome',views.welcome) #for the welcome screen

]
