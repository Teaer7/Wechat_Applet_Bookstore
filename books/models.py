from django.db import models
from users.models import UsersProfile

# Create your models here.
class BooksInfo(models.Model):
    """
    书籍信息表
    书籍id, 封面, 书名, 作者, 定价, 新旧, 状态, 出版社, 出版时间, 分类, 内容简介, 交易量, 收藏量, 点击量, 库存
    """
    CLASSI_CHOICE = [
        # 书籍分类 枚举
        (0, '待分类'),
        (1, '小说/艺术'),
        (2, '社会文化/法律'),
        (3, '文学/外国文学'),
        (4, '教育/教材/教辅'),
        (5, '军事/政治/经济'),
        (6, '历史/地理/宗教'),
        (7, '哲学/心理学'),
        (8, '科学/科技/医学/医药'),
        (9, '其他'),
    ]
    book_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='book_id')
    cover = models.ImageField(upload_to='book_image/%Y/%m', default='static/book_image/default.jpg', max_length=100, blank=True, null=True, verbose_name='封面')
    title = models.CharField(max_length=80, verbose_name='书名')
    author = models.CharField(max_length=30, verbose_name='作者')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='定价')
    new_old = models.BooleanField(default=0, choices=((0, '新'), (1, '旧')), verbose_name='新旧')
    state = models.BooleanField(default=0, choices=((0, '在售'), (1, '下架')), verbose_name='状态')
    publisher = models.CharField(max_length=80, verbose_name='出版社')
    p_date = models.DateField(blank=True, null=True, verbose_name='出版时间')
    classi = models.IntegerField(default=0, choices=CLASSI_CHOICE, verbose_name='分类')
    intro = models.TextField(null=True, blank=True, verbose_name='内容简介')
    trading_volume = models.IntegerField(default=0, verbose_name='交易量')
    collection_volume = models.IntegerField(default=0, verbose_name='收藏量')
    hit_volume = models.IntegerField(default=0, verbose_name='点击量')
    stock = models.IntegerField(default=0, verbose_name='库存')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name


class BooksCollect(models.Model):
    collect_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='collect_id')
    user = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, verbose_name='user_id')
    book = models.ForeignKey(BooksInfo, on_delete=models.DO_NOTHING, verbose_name='book_id')
    c_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.collect_id

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class BooksHit(models.Model):
    hit_id = models.AutoField(primary_key=True, auto_created=True, verbose_name='hit_id')
    user = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, verbose_name='user_id')
    book = models.ForeignKey(BooksInfo, on_delete=models.DO_NOTHING, verbose_name='book_id')
    h_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.hit_id

    class Meta:
        verbose_name = '点击信息'
        verbose_name_plural = verbose_name