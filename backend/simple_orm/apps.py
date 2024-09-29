from django.apps import AppConfig


class SimpleOrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simple_orm'
