from django.conf.urls import url, include
from books.views import bookHome, bookClassi

app_name = 'books'
urlpatterns = [
    url('bookHome/', bookHome),
    url('bookClassi/', bookClassi)
]
