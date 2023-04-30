from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "src.data.orm.db.users"
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Usuarios"