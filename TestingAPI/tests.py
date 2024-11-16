import pytest
from .models import ShopItems  

# # @pytest.mark.django_db
# def test_ShopItems():

#     item = ShopItems.objects.create(items="pen")


#     assert item.items == "pen" 
#     assert ShopItems.objects.count() == 1  

@pytest.mark.django_db
def test_shopitems_endpoint(client):
    response = client.get('shopitems/')
    assert response.status_code == 200

