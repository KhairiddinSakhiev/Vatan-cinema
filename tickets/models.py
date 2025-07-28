from django.db import models

from cinema.models import *
from accounts.models import *

class SeatCategory(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} -- {self.price}'
    
    class Meta:
        db_table = 'seatcategory'
        managed = True
        verbose_name = 'SeatCategory'
        verbose_name_plural = 'SeatCategorys' 

class SeatPlace(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    category = models.ForeignKey(SeatCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    row = models.BigIntegerField()
    call = models.BigIntegerField()

    def __str__(self):
        return f'{self.hall} -- {self.category} -- {self.is_active}'
    
    class Meta:
        db_table = 'seateplace'
        managed = True
        verbose_name = 'SeatePlace'
        verbose_name_plural = 'SeatePlaces' 

class Ticket(models.Model):
    seanse = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(SeatPlace, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.seanse} -- {self.seat}'
    
    class Meta:
        db_table = 'ticket'
        managed = True
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets' 

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=255)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} -- {self.ticket} -- Is payed: {self.payment_status}'
    
    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders' 
