from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teams:team_list')
    else:
        form = TeamForm()
    return render(request, 'teams/team_form.html', {'form': form})

def team_detail(request, pk):
    team = Team.objects.get(pk=pk)
    return render(request, 'teams/team_detail.html', {'team': team})