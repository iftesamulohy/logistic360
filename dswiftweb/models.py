from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class DeliveryCharges(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    amount = models.IntegerField()
    def __str__(self):
        return f"{self.name}"
class DeliveryItems(models.Model):
    sku = models.CharField(max_length=32, unique=True,null=True,blank=True)
    product_name  = models.CharField(max_length=200)
    description = models.TextField()
    reciever_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    destinations = models.TextField()
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    CHOICE_OPTION1 = 'Pending'
    CHOICE_OPTION2 = 'On The Way'
    CHOICE_OPTION3 = 'Confirmed'
    CHOICE_OPTION6 = 'Returned'

    CHOICES = [
        (CHOICE_OPTION1, 'Pending'),
        (CHOICE_OPTION2, 'On The Way'),
        (CHOICE_OPTION3, 'Confirmed'),
        (CHOICE_OPTION6, 'Returned'),
        
    ]
    status =  models.CharField(max_length=20, choices=CHOICES)

    CHOICE_OPTION4 = 'Due'
    CHOICE_OPTION5 = 'Completed'
    

    CHOICES2 = [
        (CHOICE_OPTION4, 'Due'),
        (CHOICE_OPTION5, 'Completed'),
        
        
    ]
    payment_status =  models.CharField(max_length=20, choices=CHOICES2)
    recieve_amount = models.IntegerField()
    assigned_deliveryman = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    delivery_charge = models.ForeignKey(DeliveryCharges,on_delete=models.CASCADE,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = str(uuid.uuid4().hex)[:32]
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.sku}"
    class Meta:
        verbose_name = "Delivery Item"
    