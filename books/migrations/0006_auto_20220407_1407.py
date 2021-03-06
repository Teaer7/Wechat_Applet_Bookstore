# Generated by Django 2.1 on 2022-04-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20220407_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinfo',
            name='classi',
            field=models.IntegerField(choices=[(0, '待分类'), (1, '小说/艺术'), (2, '社会文化/法律'), (3, '文学/外国文学'), (4, '教育/教材/教辅'), (5, '军事/政治/经济'), (6, '历史/地理/宗教'), (7, '哲学/心理学'), (8, '科学/科技/医学/医药'), (9, '其他')], default=0, verbose_name='分类'),
        ),
    ]
