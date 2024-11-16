from rest_framework import serializers
from .models import *

class ShopItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItems
        fields = '__all__'  