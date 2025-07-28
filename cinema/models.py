from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.BigIntegerField()
    latitude = models.BigIntegerField()
    longitude = models.BigIntegerField()

    def __str__(self):
        return f'{self.name} -- {self.location}'
    
    class Meta:
        db_table = 'theater'
        managed = True
        verbose_name = 'Theater'
        verbose_name_plural = 'Theaters'     

class Hall(models.Model):
    name = models.CharField(max_length=255)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    number_of_seats = models.BigIntegerField()

    def __str__(self):
        return f'{self.name} -- {self.theater.name}'
    
    class Meta:
        db_table = 'hall'
        managed = True
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls' 



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


   
