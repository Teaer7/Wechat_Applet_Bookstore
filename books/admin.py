from django.contrib import admin
from books.models import BooksInfo, BooksHit, BooksCollect


# Register your models here.
class BooksInfoAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'author', 'price', 'state', 'publisher', 'classi', 'stock')


class BooksHitAdmin(admin.ModelAdmin):
    list_display = ('hit_id', 'book_id', 'user_id', 'h_time')


class BooksCollectAdmin(admin.ModelAdmin):
    list_display = ('collect_id', 'book_id', 'user_id', 'c_time')


admin.site.register(BooksInfo, BooksInfoAdmin)
admin.site.register(BooksHit, BooksHitAdmin)
admin.site.register(BooksCollect, BooksCollectAdmin)
