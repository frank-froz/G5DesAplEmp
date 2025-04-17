from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from reviews.models import Review
from users.forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request):
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'reviews': user_reviews})

def logout_view(request):
    logout(request)
    return redirect('movie_list')
