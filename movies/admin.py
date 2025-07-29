from django.contrib import admin
<<<<<<< HEAD
from .models import Movie,Actor,MovieActor,Director,MovieDirector,Trailer

"""
=======
from .models import *

>>>>>>> 9e07eaa1105cb1c6ad94bfcce133ba2448ba5f74
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MovieActor)
admin.site.register(Director)
admin.site.register(MovieDirector)
<<<<<<< HEAD
admin.site.register(Trailer)
"""


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','description','age_limit','country','rel_year','is_active','duration')
    list_display_links = ('title',)
    fieldsets = (
        ('Info',{
            "fields":('title','description','age_limit','country','rel_year','duration','is_active'),
        }),
    )
    search_fields = ('title','age_limit','counry','rel_year','is_active')
    list_filter = ('title','age_limit','country','rel_year','is_active')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','experience','is_active',)
    list_display_links = ('name',)
    fieldsets = (
        ('Info',{
            "fields":('name','experience','is_active',),
        }),
    )
    search_fields = ('name','experience','is_active',)
    list_filter = ('name','experience','is_active',)

@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    list_display = ('movie','actor','is_hero',)
    list_display_links = ('movie',)
    fieldsets = (
        ('Info',{
            "fields":('movie','actor','is_hero',),
        }),
    )
    search_fields = ('movie','actor','is_hero',)
    list_filter = ('movie','actor','is_hero',)
    

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('fullname','is_active',)
    list_display_links = ('fullname',)
    fieldsets = (
        ('Info',{
            "fields":('fullname','is_active',),
        }),
    )
    search_fields = ('fullname','is_active',)
    list_filter = ('fullname','is_active',)

@admin.register(MovieDirector)
class MovieDirectorAdmin(admin.ModelAdmin):
    list_display = ('movie','director',)
    list_display_links = ('movie',)
    fieldsets = (
        ('Info',{
            "fields":('movie','director',),
        }),
    )
    search_fields = ('movie','director',)
    list_filter = ('movie','director',)


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('movie','is_active',)
    list_display_links = ('movie',)
    fieldsets = (
        ('Trailer_Info',{
            "fields":('movie','file','image','is_active','created_at'),
        }),
    )
    search_fields = ('movie','is_active',)
    list_filter = ('movie','is_active',)
=======
admin.site.register(Trailer)
>>>>>>> 9e07eaa1105cb1c6ad94bfcce133ba2448ba5f74
