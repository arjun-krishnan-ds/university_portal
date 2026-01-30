import os
import django
from django.db import transaction
from django.contrib.auth import get_user_model

# --- Step 0: bootstrap Django ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university_portal.settings")
django.setup()

User = get_user_model()

# --- Step 1: configure new superuser ---
new_username = "admin"              # new superuser username
new_email = "admin@example.com"     # email for new superuser
new_password = "YourNewPassword123!" # new password

# --- Step 2: create or update new superuser ---
if User.objects.filter(username=new_username).exists():
    new_user = User.objects.get(username=new_username)
    new_user.set_password(new_password)
    new_user.is_superuser = True
    new_user.is_staff = True
    new_user.save()
    print(f"Password for existing superuser '{new_username}' updated.")
else:
    new_user = User.objects.create_superuser(username=new_username, email=new_email, password=new_password)
    print(f"Superuser '{new_username}' created.")

# --- Step 3: reassign orphaned objects to new user ---
from django.apps import apps

reassigned_count = 0
with transaction.atomic():
    all_models = apps.get_models()
    for model in all_models:
        for field in model._meta.get_fields():
            # Only consider ForeignKeys pointing to User
            if field.is_relation and field.many_to_one and field.related_model == User:
                # Find objects where FK points to a missing user (NULL or invalid FK)
                filter_kwargs = {f"{field.name}__isnull": True}
                count = model.objects.filter(**filter_kwargs).update(**{field.name: new_user})
                reassigned_count += count

print(f"Reassigned {reassigned_count} orphaned objects to '{new_username}'.")
print("Done.")
