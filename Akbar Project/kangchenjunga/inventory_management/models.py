from django.db import models
from django.contrib.auth.models import User
import random
import datetime


class Equipment(models.Model):
    gadget_name = models.CharField(max_length=50, unique=True)
    gadget_model = models.CharField(max_length=50)
    gadget_label = models.CharField(max_length=50)
    gadget_serial_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    gadget_price = models.DecimalField(max_digits=10, decimal_places=2)


    # def random_equipment_data(self):
    #     g_names=['Laptop','Mouse','Keyboard','Monitor']
    #     mo=['AA','BB','CC']
    #     g_model=f'{random.choice(g_names)}{random.choice(g_names)}i'
    #     g_label=f'{random.choice(g_names)}{random.choice(g_names)}i'
    #     g_serial_number=f'{random.choice(g_names)}{random.choice(g_names)}i{datetime.now()}'
    #     purchase_date


class Inventory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)

    # def random_inventory_data(self):
