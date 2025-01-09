import json
from django.core.management.base import BaseCommand
from kanji_app.models import Kanji

class Command(BaseCommand):
    help = "Bulk upload kanji data from a JSON file"

    def handle(self, *args, **kwargs):
        json_file_path = r'C:\Kanji\unified_kanji_with_levels.json'  # Ensure this path matches the unified JSON file
        
        try:
            # Load JSON data
            with open(json_file_path, 'r', encoding='utf-8') as file:
                kanji_list = json.load(file)

            for kanji_data in kanji_list:
                # Ensure all required fields are present
                character = kanji_data.get('character')
                if not character:
                    self.stderr.write("Skipping an entry without a 'character'")
                    continue

                # Create or update the kanji entry in the database
                kanji, created = Kanji.objects.update_or_create(
                    character=character,
                    defaults={
                        'onyomi': kanji_data.get('onyomi', ""),
                        'kunyomi': kanji_data.get('kunyomi', ""),
                        'jlpt_level': kanji_data.get('jlpt_level'),  # Handles levels 1–5
                        'strokes': kanji_data.get('strokes'),
                        'meaning': kanji_data.get('meaning', ""),
                        'common_words': kanji_data.get('common_words', ""),  # Retain or handle later if needed
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added kanji: {kanji.character}"))
                else:
                    self.stdout.write(f"Updated kanji: {kanji.character}")

        except FileNotFoundError:
            self.stderr.write(f"The JSON file '{json_file_path}' was not found.")
        except json.JSONDecodeError as e:
            self.stderr.write(f"Error decoding JSON: {e}")
        except Exception as e:
            self.stderr.write(f"An unexpected error occurred: {e}")
