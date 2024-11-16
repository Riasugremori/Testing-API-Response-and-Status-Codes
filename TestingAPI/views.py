from rest_framework import viewsets
from .models import ShopItems
from .serializers import ShopItemsSerializer

class ShopItemsViewSet(viewsets.ModelViewSet):
    queryset = ShopItems.objects.all()
    serializer_class = ShopItemsSerializer
