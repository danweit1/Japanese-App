import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'japanese_app.settings')
django.setup()

from kanji_app.models import Kanji
from parse_kanjidic import parse_kanjidic  # Import the parsing function

# Path to the KanjiDic2 XML file
xml_file = 'C:/Kanji/kanjidic2.xml'  # Replace with the actual path to your XML file

# Parse the XML to get kanji data
kanji_data = parse_kanjidic(xml_file)

# Bulk insert kanji into the database
for kanji in kanji_data:
    Kanji.objects.update_or_create(
        character=kanji['character'],
        defaults={
            'onyomi': kanji['onyomi'],
            'kunyomi': kanji['kunyomi'],
            'strokes': kanji['stroke_count'],
            'jlpt_level': kanji['jlpt_level'],
            'meaning': kanji['meanings'],
        }
    )

print(f"Successfully inserted {len(kanji_data)} JLPT kanji into the database.")
