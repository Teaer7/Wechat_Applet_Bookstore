from django.conf.urls import url, include
from users.views import userIndex

app_name = 'users'
urlpatterns = [
    url('userIndex/', userIndex)
]
