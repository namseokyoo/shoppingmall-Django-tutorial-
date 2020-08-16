import datetime
import uuid
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(default=0)
    image1 = models.ImageField(blank=False)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    description = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    name = models.CharField(max_length=5)
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.PositiveIntegerField(default=0)
    phone_number = PhoneNumberField()
    order_date = models.DateTimeField(auto_now_add=True)
    email= models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    delivered = models.BooleanField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
