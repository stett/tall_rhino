from django.contrib import admin
from .models import *

class PostImageInline(admin.TabularInline):
    model = PostImage
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (PostImageInline, )
    prepopulated_fields = {"slug": ("title", )}
admin.site.register(Post, PostAdmin)

admin.site.register(PostImage)

admin.site.register(PostComment)
