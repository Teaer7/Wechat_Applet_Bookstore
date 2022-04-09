from django.db import models
from users.models import UsersProfile
from books.models import BooksInfo

# Create your models here.
class CartsInfo(models.Model):
    cart_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='cart_id')
    user = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, verbose_name='user_id')
    book = models.ForeignKey(BooksInfo, on_delete=models.DO_NOTHING, verbose_name='book_id')
    book_price = models.DecimalField(default=0, max_digits=6, decimal_places=2, verbose_name='书籍单价')
    cart_quantity = models.IntegerField(default=1, verbose_name='入车数量')
    cart_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='入车总额')
    cart_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.cart_id

    class Meta:
        verbose_name = '购物车信息'
        verbose_name_plural = verbose_name
