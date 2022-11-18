from django.contrib import admin
# from django.contrib.admin import decorators

from .models import Company, Product
from users.models import User


@admin.action(description='Очищает задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'provider', 'debt')
    list_filter = ('city',)
    actions = [clear_debt]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product)
admin.site.register(User)
