from django.contrib import admin
from users.models import UsersProfile

# Register your models here.
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'email', 'gender', 'is_student', 'book_hobby', 'point')

admin.site.register(UsersProfile, UsersProfileAdmin)
