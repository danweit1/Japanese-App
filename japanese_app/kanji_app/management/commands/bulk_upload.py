import json
from django.core.management.base import BaseCommand
from kanji_app.models import Kanji

class Command(BaseCommand):
    help = "Bulk upload kanji data from a JSON file"

    def handle(self, *args, **kwargs):
        try:
            with open('kanji_data.json', 'r', encoding='utf-8') as file:
                kanji_list = json.load(file)
                for kanji_data in kanji_list:
                    kanji, created = Kanji.objects.get_or_create(
                        character=kanji_data['character'],
                        defaults={
                            'onyomi': kanji_data['onyomi'],
                            'kunyomi': kanji_data['kunyomi'],
                            'jlpt_level': kanji_data['jlpt_level'],
                            'strokes': kanji_data['strokes'],
                            'meaning': kanji_data['meaning'],
                            'common_words': kanji_data['common_words'],
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Added kanji: {kanji.character}"))
                    else:
                        self.stdout.write(f"Kanji {kanji.character} already exists")
        except FileNotFoundError:
            self.stderr.write("The 'kanji_data.json' file was not found.")
        except json.JSONDecodeError as e:
            self.stderr.write(f"Error decoding JSON: {e}")
