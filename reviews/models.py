from django.db import models
from accounts.models import *
from movies.models import *

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    star_number = models.BigIntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.movie.title}"
    
    class Meta:
        db_table = 'review'
        managed = True
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'