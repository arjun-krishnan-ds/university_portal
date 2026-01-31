import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from core.models import Faculty   # change app name


def run():
    qs = Faculty.objects.exclude(f_img="")

    print(f"Found {qs.count()} faculty image entries")

    for f in qs:
        f.f_img = None
        f.save(update_fields=["f_img"])

    print("All Faculty image fields cleared.")


if __name__ == "__main__":
    run()
