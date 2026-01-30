import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university_portal.settings")
django.setup()

with open("db.json", "w", encoding="utf-8") as f:
    call_command("dumpdata", "auth.user", "core", indent=2, stdout=f)

print("done")
