# your_app/management/commands/upload_faculty_to_cloudinary.py

from django.core.management.base import BaseCommand
from core.models import Faculty  # Replace with your actual app name
from django.core.files import File
import os

class Command(BaseCommand):
    help = "Upload existing local faculty images to Cloudinary and update DB"

    def handle(self, *args, **kwargs):
        faculties = Faculty.objects.all()
        for f in faculties:
            if f.f_img and not f.f_img.url.startswith("http"):
                local_path = f.f_img.path
                if os.path.exists(local_path):
                    with open(local_path, "rb") as file:
                        f.f_img.save(os.path.basename(local_path), File(file), save=True)
                    self.stdout.write(f"[✅] Uploaded {f.f_name} → {f.f_img.url}")
                else:
                    self.stdout.write(f"[⚠️] File missing: {local_path}")
            else:
                self.stdout.write(f"[ℹ️] Already on Cloudinary: {f.f_name}")
