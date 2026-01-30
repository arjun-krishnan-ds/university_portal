from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        # Import signals here to avoid duplicate model registration
        import core.signals


class AdmissionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admissions"
