from django.contrib import admin

from .models import Company, Product
from users.models import User


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(User)

