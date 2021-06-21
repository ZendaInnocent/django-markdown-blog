from django.contrib import admin

from posts.models import Post, Tag

admin.site.site_title = 'Elegant Tech Admin'
admin.site.site_header = 'Elegant Tech Administration'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'created_on', 'updated_on', ]
    search_fields = ['title', 'excerpt', 'content', 'tags__name', ]
    list_filter = ['created_on', 'updated_on', ]
    list_select_related = True
    save_on_top = True
    filter_horizontal = ['tags', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
