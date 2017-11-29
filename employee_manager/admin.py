from django.contrib import admin
from .models import ProfileEmployee

class ProfileAdmin(admin.ModelAdmin):
    """
    Whit this class we can define what and how will be showed in the admin
    page
    """

    # fields = ['name', 'email', 'department']
    fieldsets = [
        ('Employee name',               {'fields': ['name']}),
        ('Employee information', {'fields': ['email', 'department']}),
    ]
    # displayed fields
    list_display = ('name', 'department', 'email')
    # highlighted field in the page
    list_filter = ['department']

admin.site.register(ProfileEmployee, ProfileAdmin)
