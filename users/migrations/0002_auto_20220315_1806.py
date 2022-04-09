# Generated by Django 2.1 on 2022-03-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='usersprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersprofile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='gender',
            field=models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0, max_length=1, verbose_name='性别'),
        ),
    ]