from django.urls import path
from . import views

urlpatterns = [

    path('signup',views.signup,nname = 'signup'),
    path('login',views.login,nname = 'login'),
    path('logout',views.logout,nname = 'logout')



]