from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('author', 'created_at')
    fields = ('author', 'content', 'is_approved', 'created_at')
    can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'comment_count', 'display_image')
    list_filter = ('status', 'category', 'created_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CommentInline]
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'featured_image')
        }),
        ('Relationships', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Publishing Options', {
            'fields': ('status', 'published_at', 'created_at', 'updated_at')
        }),
    )
    
    def display_image(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.featured_image.url)
        return "No image"
    display_image.short_description = "Featured Image"
    
    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('content', 'author__username', 'post__title')
    date_hierarchy = 'created_at'
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} comments have been approved.')
    approve_comments.short_description = "Approve selected comments"