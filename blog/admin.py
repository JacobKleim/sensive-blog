from django.contrib import admin

from blog.models import Comment, Post, Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
    list_display = ('author', 'post',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes',)


admin.site.register(Tag)
