from django.db import models
from users.models import UsersProfile
from books.models import BooksInfo

# Create your models here.
class OrdersInfo(models.Model):
    order_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='order_id')
    user = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, verbose_name='user_id')
    book = models.ForeignKey(BooksInfo, on_delete=models.DO_NOTHING, verbose_name='book_id')
    book_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='书籍单价')
    o_quantity = models.IntegerField(default=0, verbose_name='购入数量')
    o_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='订单总额')
    o_state = models.IntegerField(default=0, choices=((0, '待付款'), (1, '已付款'), (2, '待发货'), (3, '待收货'), (4, '已完成')), verbose_name='订单状态')
    o_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = '购入信息'
        verbose_name_plural = verbose_name


class SellInfo(models.Model):
    sell_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='sell_id')
    user = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, verbose_name='user_id')
    book = models.ForeignKey(BooksInfo, on_delete=models.DO_NOTHING, verbose_name='book_id')
    book_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='书籍单价')
    s_quantity = models.IntegerField(default=0, verbose_name='卖出数量')
    s_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='卖单总额')
    s_state = models.IntegerField(default=0, choices=((0, '待发布'), (1, '待审核'), (2, '已完成')), verbose_name='卖单状态')
    s_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.sell_id

    class Meta:
        verbose_name = '卖出信息'
        verbose_name_plural = verbose_name