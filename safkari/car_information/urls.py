from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Cars_list/',views.CarsList.as_view(),name="Cars_list"),
    path('CarEdit/',views.CarEdit.as_view(),name="Car_edit"),
    path('Car_owner_list/',views.CarOwnersList.as_view(),name="Car_owner_list"),
    path('Car_owner_edit/',views.CarOwnerEdit.as_view(),name="Car_owner_edit"),
]