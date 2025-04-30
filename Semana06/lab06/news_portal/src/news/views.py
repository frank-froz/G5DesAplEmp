from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
class ArticleListView(ListView):
    """View for listing articles on the home page"""
    model = Article
    template_name = "news/home.html"
    context_object_name = "latest_articles"
    
    def get_queryset(self):
        """Get only published articles"""
        return Article.objects.filter(status="published")
    
    def get_context_data(self, **kwargs):
        """Add categories and recent articles to context"""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]
        return context


class ArticleDetailView(DetailView):
    """View for displaying a single article"""
    model = Article
    template_name = "news/article_detail.html"
    context_object_name = "article"
    
    def get_queryset(self):
        """Get only published articles"""
        return Article.objects.filter(status="published")
    
    def get_context_data(self, **kwargs):
        """Add categories and recent articles to context"""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]
        return context
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    """View for creating new articles"""
    model = Article
    template_name = "news/article_form.html"
    fields = ['title', 'content', 'image', 'category', 'status']
    success_url = reverse_lazy('news:home')
    
    def form_valid(self, form):
        """Set the author to the current user before saving"""
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """View for editing existing articles"""
    model = Article
    template_name = "news/article_form.html"
    fields = ['title', 'content', 'image', 'category', 'status']
    
    def get_success_url(self):
        """Redirect to the article detail page after editing"""
        return reverse_lazy('news:article_detail', kwargs={'slug': self.object.slug})
    
    def get_queryset(self):
        """Only allow editing of articles by their author"""
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)