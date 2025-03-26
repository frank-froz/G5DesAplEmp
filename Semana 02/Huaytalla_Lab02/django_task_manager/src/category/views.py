from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Category
from .forms import CategoryForm

# Listar categorías
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

# Crear categoría
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/form.html', {'form': form})

# Editar categoría
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/form.html', {'form': form})

# Eliminar categoría
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/confirm_delete.html', {'category': category})
