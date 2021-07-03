from django.contrib import admin
from blog.models import Comment, Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    pass


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on')
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentsAdmin)
