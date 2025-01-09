import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japanese_app.settings")  # Replace 'japanese_app.settings' with your project's settings module
django.setup()

import requests
from kanji_app.models import Kanji

# Jisho.org API Base URL
API_BASE = "https://kanjiapi.dev/v1/kanji"

# Function to fetch data for a single kanji
def fetch_kanji_data(character):
    try:
        response = requests.get(f"{API_BASE}/{character}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch {character}: Status {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching {character}: {e}")
        return None

# Update common words in the database
def update_common_words():
    for kanji in Kanji.objects.all():
        print(f"Fetching data for {kanji.character}...")
        data = fetch_kanji_data(kanji.character)

        if data and "examples" in data:
            examples = data["examples"]
            kanji.common_words = ", ".join(examples) if examples else None
            kanji.save()
            print(f"Updated {kanji.character} with examples: {examples}")
        else:
            print(f"No examples found for {kanji.character}")

if __name__ == "__main__":
    update_common_words()
