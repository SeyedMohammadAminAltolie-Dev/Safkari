from django.urls import path, include
from . import views

urlpatterns = [
    path('repair_request_list/',views.RepaireRequestList.as_view(),name="Repair_requests_list"),
    path('repair_request_edit/',views.RepaireRequestEdit.as_view(),name="Repair_requests_edit"),
    path('repair_item_list/',views.RepaireItemList.as_view(),name="Repair_item_list"),
    path('repair_item_edit/',views.RepaireItemEdit.as_view(),name="Repair_item_edit"),
    path('new_payment/',views.NewPayment.as_view(),name="New_payment"),
    path('payment_edit/',views.PaymentEdit.as_view(),name="payment_edit"),
    path('payment_liest/',views.PaymentList.as_view(),name="payment_list"),
    path('new_album/',views.NewAlbum.as_view(),name="New_Album"),
    path('album_list/',views.AlbumList.as_view(),name="album_list"),
    path('album_edit/',views.AlbumEdit.as_view(),name="album_edit"),
    path('new_Image/',views.NewImage.as_view(),name="new_Image"),
    path('image_edit/',views.ImageEdit.as_view(),name="Image_edit"),
    path('image_list/',views.ImageEdit.as_view(),name="Image_list"),
]