from rest_framework import serializers
from .models import Repair_Request,RepairItem,ExtraItems,Album,Image ,Payment

class RepairRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair_Request
        fields = '__all__'

class RepairItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairItem
        fields = '__all__'

class ExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItems
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'