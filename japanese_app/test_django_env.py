import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japanese_app.settings")  # Adjust this path if needed
django.setup()

from kanji_app.models import Kanji

print("Django environment loaded successfully!")
print(f"Total kanji in database: {Kanji.objects.count()}")
