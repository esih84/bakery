from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [

    path('register', Register, name="register"),
    path('seller_register', RegisterSeller, name="sellerRegister"),
    path('login', Login, name="login"),
    path('logout', Logout, name="logout"),
    path('edit_profile', editProfile, name="edit_profile"),
    path('seller_edit_profile', SellerEditProfile, name="seller_edit_profile"),
    path('profile_view', profile, name="profile_view"),
    path('login_phone/', login_phone, name="login_phone"),
    path('verify_login_phone/', verify_login_phone, name="verify_login_phone"),

]
