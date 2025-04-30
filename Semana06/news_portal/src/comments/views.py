from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from news.models import Article  # si tu modelo de artículos está en la app "news"

def post_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form})
