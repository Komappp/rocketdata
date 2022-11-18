from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'company')
    list_display_links = ('username', 'company')
    list_filter = ('company',)


admin.site.register(User, UserAdmin)
