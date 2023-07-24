from django.urls import path
from .views import registerPage , loginPage , logoutPage , homePage

urlpatterns = [
    path('',loginPage, name='loginPage'),
    path('home/',homePage, name='homePage'),
    path('login/',loginPage, name='loginPage'),
    path('logout/',logoutPage, name='logoutPage'),
    path('register/',registerPage, name='registerPage'),
]