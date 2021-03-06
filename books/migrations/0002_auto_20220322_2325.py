# Generated by Django 2.1 on 2022-03-22 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksCollect',
            fields=[
                ('collect_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='collect_id')),
                ('c_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': '收藏信息',
                'verbose_name_plural': '收藏信息',
            },
        ),
        migrations.CreateModel(
            name='BooksHit',
            fields=[
                ('hit_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='hit_id')),
                ('c_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': '点击信息',
                'verbose_name_plural': '点击信息',
            },
        ),
        migrations.AlterModelOptions(
            name='booksinfo',
            options={'verbose_name': '书籍信息', 'verbose_name_plural': '书籍信息'},
        ),
        migrations.AddField(
            model_name='bookshit',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.BooksInfo'),
        ),
        migrations.AddField(
            model_name='bookshit',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookscollect',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.BooksInfo'),
        ),
        migrations.AddField(
            model_name='bookscollect',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
