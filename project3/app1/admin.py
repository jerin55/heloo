from django.contrib import admin

from app1.models import *

# Register your models here.


admin.site.register(customers)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)