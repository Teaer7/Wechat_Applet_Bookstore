from django.contrib import admin
from orders.models import OrdersInfo, SellInfo

# Register your models here.
admin.site.register(OrdersInfo)
admin.site.register(SellInfo)

