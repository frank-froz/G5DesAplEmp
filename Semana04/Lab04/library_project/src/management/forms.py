# management/forms.py
from django import forms
from .models import LibraryBranch

class LibraryBranchForm(forms.ModelForm):
    class Meta:
        model = LibraryBranch
        fields = '__all__'
