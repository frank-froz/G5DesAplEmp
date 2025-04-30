from django.apps import AppConfig


from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'  # Este es el path
    label = 'user_profiles'  # 👈 Este es el identificador único para Django

    def ready(self):
        import profiles.signals  # 👈 Aquí se activa
