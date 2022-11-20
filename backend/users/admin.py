from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'company_link')
    list_display_links = ('username', )
    list_filter = ('company',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1',
                       'password2', 'first_name',
                       'last_name', 'email', 'company',
                       'is_staff', 'is_active')}),
    )

    def company_link(self, obj):

        if obj.company:
            return mark_safe(
                f"<a href='/admin/companies/company/{obj.company.id}/change/'>"
                f"{obj.company}"
                f"</a>"
            )


admin.site.register(User, UserAdmin)
