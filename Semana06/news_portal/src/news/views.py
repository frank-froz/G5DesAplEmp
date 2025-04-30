from django.shortcuts import render, get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


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

        from django.shortcuts import redirect

def post_comment(request):
    if request.method == "POST":
        # Aquí manejas la lógica de guardado del comentario
        # ...
        return redirect('article_detail', slug='some-slug')  # o como manejes la redirección


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'news/register.html', {'form': form})




@login_required
def post_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Asigna el usuario autenticado
            comment.article = article
            comment.save()
            return redirect('news:article_detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'comments/comment_form.html', {'form': form, 'article': article})
