from django.contrib import admin
from .models import Equipment,Inventory
# Register your models here.


@admin.register(Equipment)
class EmployeeAdminClass(admin.ModelAdmin):
    list_display=[  'gadget_name',
                    'gadget_model',
                    'gadget_label',
                    'gadget_serial_number',
                    'purchase_date',
                    'gadget_price'
                ]

    
@admin.register(Inventory)
class InventoryAdminClass(admin.ModelAdmin):
    list_display=[ 'assigned_date',
                    'returned_date'
                ]
