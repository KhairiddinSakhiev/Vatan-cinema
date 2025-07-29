from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('register/', register_view, name='register'),
    path('confirm-email/<uuid:token>/', confirm_email, name='confirm_email'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('reset-password/', reset_password_view, name='reset_password'),
    path('reset-password-confirm/<uuid:token>/', reset_password_confirm_view, name='reset_password_confirm'),
    path('change-password/', change_password_view, name='change_password'),

  
    path('profile/create/', profile_create_view, name='profile_create'),
    path('profile/', profile_detail_view, name='profile_detail'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
]
