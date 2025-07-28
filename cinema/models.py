from django.db import models
from movies.models import Movie

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
