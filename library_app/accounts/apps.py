from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library_app.accounts'

    def ready(self):
        import library_app.accounts.signals
        result = super().ready()
        return result
