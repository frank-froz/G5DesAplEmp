from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Post, Category, Tag, Comment


class PostListView(ListView):
    """View for listing all published blog posts"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Return all published posts"""
        return Post.blog_objects.published()
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(
            posts_count=Count('posts')
        )
        context['tags'] = Tag.objects.annotate(
            posts_count=Count('posts')
        ).order_by('-posts_count')[:10]
        context['recent_posts'] = Post.blog_objects.recent_posts()
        return context


class PostDetailView(DetailView):
    """View for displaying a single post with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        """Ensure we only show published posts"""
        return Post.blog_objects.published()
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(is_approved=True)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(
            posts_count=Count('posts')
        ).order_by('-posts_count')[:10]
        context['recent_posts'] = Post.blog_objects.recent_posts().exclude(
            id=self.object.id
        )
        return context


class CategoryPostListView(ListView):
    """View for listing posts in a specific category"""
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Get posts for the specified category"""
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return Post.blog_objects.by_category(self.category.slug)
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.annotate(
            posts_count=Count('posts')
        )
        context['tags'] = Tag.objects.annotate(
            posts_count=Count('posts')
        ).order_by('-posts_count')[:10]
        return context


class TagPostListView(ListView):
    """View for listing posts with a specific tag"""
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        """Get posts for the specified tag"""
        self.tag = Tag.objects.get(slug=self.kwargs['slug'])
        return Post.blog_objects.by_tag(self.tag.slug)
    
    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.annotate(
            posts_count=Count('posts')
        ).order_by('-posts_count')[:10]
        return context