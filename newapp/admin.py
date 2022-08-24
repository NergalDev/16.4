from django.contrib import admin
from .models import Author, Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'dateCreation', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
