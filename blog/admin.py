from django.contrib import admin

from .models import Post, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ('post',)
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'created_at', 'status')


    list_filter = ('created_at', 'category', "status")

    search_fields = ['title', 'category__title']

    prepopulated_fields = {'slug': ('title',)}

    inlines = [CommentInline,]

    fieldsets = (
        (None, {
            'fields': ("title", "slug"),
        }),
        ("Post Details", {
            'fields': ("intro", "body", "category", "image", "status")
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')

    list_filter = ('created_at',)

    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

    search_fields = ('title', 'slug')

    prepopulated_fields = {'slug': ('title',)}

