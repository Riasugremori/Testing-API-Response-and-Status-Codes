from django.db import models

class ShopItems(models.Model):
    items = models.CharField(max_length=250) 
  
