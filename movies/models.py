from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    age_limit = models.CharField(max_length=3)
    image = models.ImageField(upload_to='media/movies/')
    duration = models.BigIntegerField()
    country = models.CharField(max_length=100)
    rel_year = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} -- {self.is_active}'
    
    class Meta:
        db_table = 'movie'
        managed = True
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies' 

class Actor(models.Model):
    name = models.CharField(max_length=255)
    experience = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} -- {self.is_active}'
    
    class Meta:
        db_table = 'actor'
        managed = True
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors' 

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    is_hero = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.movie.title} -- {self.actor.name}'
    
    class Meta:
        db_table = 'movieactor'
        managed = True
        verbose_name = 'MovieAcotor'
        verbose_name_plural = 'MovieAcotors' 

class Director(models.Model):
    fullname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname} -- {self.is_active}'
    
    class Meta:
        db_table = 'director'
        managed = True
        verbose_name = 'Director'
        verbose_name_plural = 'Directors' 

class MovieDirector(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.title} -- {self.director.fullname}'
    
    class Meta:
        db_table = 'moviedirector'
        managed = True
        verbose_name = 'MovieDirector'
        verbose_name_plural = 'MovieDirectors' 

class Trailer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/trailers/')
    image = models.ImageField(upload_to='media/trailer_thumbnails/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.title} -- {self.is_active}'
    
    class Meta:
        db_table = 'trailer'
        managed = True
        verbose_name = 'Trailer'
        verbose_name_plural = 'Trailers'     
