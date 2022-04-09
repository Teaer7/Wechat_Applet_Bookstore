from django.conf.urls import url, include
from orders.views import orderIndex

app_name = 'orders'
urlpatterns = [
    url('orderIndex/', orderIndex)
]
