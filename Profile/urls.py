from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile, name='profile'),
    path('edit/', views.EditProfile, name='editprofile'),
    path('confirm-delete-profile/', views.confirm_delete_profile, name='confirm_delete_profile'),
    path('account-deleted/', views.account_deleted, name='account_deleted'),

]
