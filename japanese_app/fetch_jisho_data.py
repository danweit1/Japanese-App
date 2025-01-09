import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japanese_app.settings")
django.setup()

import requests
from kanji_app.models import Kanji

# Jisho.org Kanji API Base URL
API_BASE = "https://kanjiapi.dev/v1/kanji"

# Function to fetch data from the API
def fetch_kanji_data(character):
    url = f"{API_BASE}/{character}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        return None

# Update kanji in the database with common words
def update_kanji_with_common_words():
    for kanji in Kanji.objects.all():
        print(f"Fetching data for {kanji.character}...")
        data = fetch_kanji_data(kanji.character)
        
        if data:
            # Extract example words
            examples = data.get("examples", [])
            kanji.common_words = ", ".join(examples) if examples else None
            kanji.save()
            print(f"Updated {kanji.character} with examples: {examples}")
        else:
            print(f"Failed to fetch data for {kanji.character}")

if __name__ == "__main__":
    update_kanji_with_common_words()
