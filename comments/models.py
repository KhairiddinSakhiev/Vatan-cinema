from django.db import models
from accounts.models import CustomUser
from movies.models import Movie

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)