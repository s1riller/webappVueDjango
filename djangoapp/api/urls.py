from django.contrib import admin
from django.urls import path, include
from .views import  CustomUserCreateView, ConfirmRegistrationView
urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('registeruser/', CustomUserCreateView.as_view(), name='user-create'),
    path('confirm-registration/<str:token>/', ConfirmRegistrationView.as_view(), name='confirm_registration'),

]


