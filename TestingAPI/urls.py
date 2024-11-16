from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopItemsViewSet


router = DefaultRouter()
router.register(r'shopitems', ShopItemsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
]
