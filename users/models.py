from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsersProfile(AbstractUser):
    """
    用户档案表
    """
    HOBBY_CHOICE = [
        # 爱好分类 枚举
        (0, '保密'),
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
    nick_name = models.CharField(max_length=20, verbose_name='昵称')
    phone = models.CharField(max_length=11, verbose_name='手机')
    gender = models.IntegerField(default=0, choices=((0, '保密'), (1, '男'), (2, '女')), verbose_name='性别')
    head_image = models.ImageField(upload_to='user_image/%Y/%m', default='static/user_image/default.jpg', max_length=100, verbose_name='头像')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='地址')
    birth = models.DateField(null=True, blank=True, verbose_name='生日')
    is_student = models.BooleanField(default=False, verbose_name='student status')
    point = models.IntegerField(default=0, verbose_name='积分')
    book_hobby = models.IntegerField(default=0, choices=HOBBY_CHOICE, verbose_name='书籍爱好')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户档案'
        verbose_name_plural = verbose_name