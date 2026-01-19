from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"


class AdmissionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admissions"

    def ready(self):
        import core.signals
