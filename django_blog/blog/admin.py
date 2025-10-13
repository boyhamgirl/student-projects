from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
list_display = ("title", "author", "published", "created")
prepopulated_fields = {"slug": ("title",)}
search_fields = ("title", "body")
list_filter = ("published", "created")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
list_display = ("post", "author", "created")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
prepopulated_fields = {"slug": ("name",)}
