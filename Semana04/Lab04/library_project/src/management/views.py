# management/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import LibraryBranch
from .forms import LibraryBranchForm

def branch_list(request):
    branches = LibraryBranch.objects.all()
    return render(request, 'management/branch_list.html', {'branches': branches})

def branch_create(request):
    if request.method == 'POST':
        form = LibraryBranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = LibraryBranchForm()
    return render(request, 'management/branch_form.html', {'form': form})

def branch_update(request, pk):
    branch = get_object_or_404(LibraryBranch, pk=pk)
    if request.method == 'POST':
        form = LibraryBranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = LibraryBranchForm(instance=branch)
    return render(request, 'management/branch_form.html', {'form': form})

def branch_delete(request, pk):
    branch = get_object_or_404(LibraryBranch, pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'management/branch_confirm_delete.html', {'branch': branch})
