from django.urls import path
from .views import registerPage , loginPage , logoutPage , homePage , qr_code_api

urlpatterns = [
    path('',loginPage, name='loginPage'),
    path('home/',homePage, name='homePage'),
    path('login/',loginPage, name='loginPage'),
    path('logout/',logoutPage, name='logoutPage'),
    path('register/',registerPage, name='registerPage'),
    path('api/qr-code/',qr_code_api, name='qrCodeApi'),
]
