from django.apps import AppConfig

# Configuration class for the 'polls' Django app
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
