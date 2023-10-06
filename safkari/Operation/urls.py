from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('users_list/',views.Users_list.as_view(),name="Users_list"),
    path('new_user/',views.NewUser.as_view(),name="New_User"),
    path('user_edit/',views.UserEdit.as_view(),name="User_Edit"),
]