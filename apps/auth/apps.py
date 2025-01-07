from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auth'
    label = 'auth_'  # допомагає уникнути конфлікту апки auth яку ми створили і апки auth всередині моделі djangorestframework
