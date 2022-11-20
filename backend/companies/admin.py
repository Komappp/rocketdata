from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Company, Product


@admin.action(description='Очиcтить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('hierarchy', 'name', 'country', 'city', 'provider_link', 'debt')
    list_display_links = ('name', )
    list_filter = ('city', 'hierarchy')
    actions = [clear_debt]

    def provider_link(self, obj):

        if obj.provider:
            return mark_safe(
                f"<a href='/admin/companies/company/{obj.provider.id}/change/'>"
                f"{obj.provider}"
                f"</a>"
            )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
