# Generated by Django 2.1 on 2022-03-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220315_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofile',
            name='book_hobby',
            field=models.IntegerField(choices=[(0, '保密'), (1, '文学')], default=0, verbose_name='书籍爱好'),
        ),
        migrations.AddField(
            model_name='usersprofile',
            name='point',
            field=models.IntegerField(default=0, verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='gender',
            field=models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='student status'),
        ),
    ]
