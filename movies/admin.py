from django.contrib import admin
from .models import Movie,Actor,MovieActor,Director,MovieDirector,Trailer


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
