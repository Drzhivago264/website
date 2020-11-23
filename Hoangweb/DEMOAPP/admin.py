from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Post, Comment
admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added', 'updated')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Item, MyModelAdmin)

admin.site.register(Comment, CommentAdmin)