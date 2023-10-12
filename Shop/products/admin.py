from django.contrib import admin
from.models import product
from.models import Category,CartItem


admin.site.register(product)
admin.site.register(Category)
admin.site.register(CartItem)

