from django import forms
from .models import LibraryBranch

class LibraryBranchForm(forms.ModelForm):
    class Meta:
        model = LibraryBranch
        fields = ['name', 'address', 'phone', 'email', 'opening_hours']
