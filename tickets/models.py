from django.db import models

from cinema.models import *
from accounts.models import *
from movies.models import Movie


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    showing_time = models.TimeField()
    showing_date = models.DateField()

    def __str__(self):
        return f'{self.movie} -- {self.hall.name} -- {self.showing_date} '
    
    class Meta:
        db_table = 'show'
        managed = True
        verbose_name = 'Show'
        verbose_name_plural = 'Shows'  


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