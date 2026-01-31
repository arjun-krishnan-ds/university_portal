import os
import django
import cloudinary
import cloudinary.api
import cloudinary.uploader
from django.utils.text import slugify

# -----------------------------
# Setup Django
# -----------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from core.models import Faculty  # replace your_app with actual app name

# -----------------------------
# Setup Cloudinary
# -----------------------------
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

# -----------------------------
# Rename Faculty Images
# -----------------------------
faculties = Faculty.objects.exclude(f_img='')  # only faculties with images

for f in faculties:
    if not f.f_img:
        continue

    old_public_id = f.f_img.public_id
    ext = f.f_img.name.split('.')[-1]
    new_public_id = f"faculty/{slugify(f.f_name)}.{ext}"

    if old_public_id != new_public_id:
        try:
            print(f"Renaming {old_public_id} -> {new_public_id}")
            cloudinary.api.rename(
                old_public_id,
                new_public_id,
                invalidate=True  # clears CDN cache
            )
        except Exception as e:
            print(f"Error renaming {old_public_id}: {e}")
