from django.apps import AppConfig
AppConfig.default = False



class PrincipalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'principal'
