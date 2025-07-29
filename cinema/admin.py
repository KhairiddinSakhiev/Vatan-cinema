from django.contrib import admin
from .models import Theater,Hall,SeatCategory,SeatPlace


#admin.site.register(Hall)
#admin.site.register(SeatCategory)
#admin.site.register(SeatPlace)
#admin.site.register(Theater)


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','theater','number_of_seats')
    list_display_links = ('name','theater')
    fieldsets = (
        ('Info',{
            "fields":('name','theater','number_of_seats'),
        }),
    )
    search_fields = ('name','theater')
    list_filter = ('name','theater')

@admin.register(SeatCategory)
class SeatCategoryAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','price',)
    list_display_links = ('name',)
    fieldsets = (
        ('Info',{
            "fields":('name','price'),
        }),
    )
    search_fields = ('name','price')
    list_filter = ('name','price')


@admin.register(SeatPlace)
class SeatPlaceAdmin(admin.ModelAdmin):
    pass
    list_display = ('hall','category','is_active','row','call')
    list_display_links = ('hall',)
    fieldsets = (
        ('Info',{
            "fields":('hall','category'),
        }),
        ('Seats_Info',{
            "fields":('is_active','row','call'),
        }),
    )
    search_fields = ('hall','category','is_active')
    list_filter = ('hall','category','is_active','row','call')


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name','location','latitude','longitude',)
    list_display_links = ('name',)
    fieldsets = (
        ('Info',{
            "fields":('name',),
        }),
        ('Location_Info',{
            "fields":('location','latitude','longitude'),
        }),
    )
    search_fields = ('name','location')
    list_filter = ('name','location')
    