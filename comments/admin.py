from django.contrib import admin
from .models import Comment

#admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','movie','description',)
    list_display_links = ('user',)
    fieldsets = (
        ('Comment_Info',{
            "fields":('user','movie','description'),
        }),
    )
    search_fields = ('user','movie')
    list_filter = ('user','movie')