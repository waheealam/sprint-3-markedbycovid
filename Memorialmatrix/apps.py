from django.apps import AppConfig


class MemorialmatrixConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Memorialmatrix'

    def ready(self):
        import Memorialmatrix.signals
