from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Si no quieres las restricciones complicadas en contraseñas, puedes eliminar esta función
def validate_password_strength(password):
    if len(password) < 4:  # Hacer la contraseña solo mínimo de 4 caracteres
        raise forms.ValidationError('La contraseña debe tener al menos 4 caracteres.')
    return password

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electrónico')
    password1 = forms.CharField(validators=[validate_password_strength])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Agregar clases a los campos para estilizar con Bootstrap
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
