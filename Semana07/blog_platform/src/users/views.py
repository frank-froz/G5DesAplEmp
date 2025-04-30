from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm  # Importa el formulario estándar o usa uno personalizado
from django.contrib.auth.views import LogoutView
from users.forms import CustomUserCreationForm 
from django.urls import reverse_lazy

# Vista de Registro (usando CreateView)
class RegisterView(CreateView):
    form_class = CustomUserCreationForm  # Usar el formulario personalizado
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:post_list')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Inicia sesión automáticamente
        messages.success(self.request, '¡Registro exitoso! Ya has iniciado sesión.')
        return super().form_valid(form)
# Vista de Login (personalizada)
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Evita que usuarios logueados vean el login
    success_url = reverse_lazy('blog:post_list')  
    def get_success_url(self):
        # Verifica si hay un parámetro 'next' en la URL, y redirige a esa página si existe
        return self.request.GET.get('next', self.success_url)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('blog:post_list')  