from django.conf.urls import url, include
from carts.views import cartIndex

app_name = 'carts'
urlpatterns = [
    url('cartIndex/', cartIndex)
]
