from django.contrib import admin
from dynamo_blogger.models import Category, Post, Comment, PostAuthor, Newsletter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass