from django.contrib import admin

from dswiftweb.models import DeliveryCharges, DeliveryItems, Unit

# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(DeliveryCharges)
class DeliveryChargesAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(DeliveryItems)
class DeliveryItemAdmin(admin.ModelAdmin):
    list_display = ['sku','status','payment_status','recieve_amount','reciever_name','phone_no']

