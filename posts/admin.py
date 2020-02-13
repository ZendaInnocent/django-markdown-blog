from django.contrib import admin

from posts.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
