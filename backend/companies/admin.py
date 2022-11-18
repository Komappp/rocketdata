from django.contrib import admin

from .models import Company, Product


@admin.action(description='Очищает задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'provider', 'debt')
    list_display_links = ('name', 'provider')
    list_filter = ('city',)
    actions = [clear_debt]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
