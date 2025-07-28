from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','username','date_joined','last_login','is_superuser','is_active','is_staff',)
    list_display_links = ('email','username')
    fieldsets = (
        ('Registration_Info',{
            "fields":('email','password'),
        }),
        ('Extra_Info',{
            "fields":('first_name','last_name'),
        }),
        ('Status_Info',{
            "fields":('is_superuser','is_active','is_staff'),
        }),
        ('Active_Info',{
            "fields":('date_joined','last_login'),
        }),
    )
    search_fields = ('email','is_superuser')
    list_filter = ('email','is_superuser')
