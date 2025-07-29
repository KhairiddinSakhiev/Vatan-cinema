from django.contrib import admin
from .models import Review

#admin.site.register(Review)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie','user','star_number','is_active',)
    list_display_links = ('movie',)
    fieldsets = (
        ('Trailer_Info',{
            "fields":('movie','user','star_number','description','is_active','created_at'),
        }),
    )
    search_fields = ('movie','user','is_active')
    list_filter = ('movie','user','is_active',)