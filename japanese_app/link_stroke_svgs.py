import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japanese_app.settings")
django.setup()

from kanji_app.models import Kanji

# Path to the KanjiVG SVG folder
SVG_FOLDER = "C:/Kanji/VG/kanjivg-master/kanji"  # Replace with your path

# Function to get the Unicode hex filename of a kanji
def get_svg_filename(character):
    unicode_hex = f"{ord(character):05X}.svg"  # Ensure 5 characters with leading zero
    return unicode_hex

# Link SVGs to kanji in the database
def link_svgs_to_kanji():
    for kanji in Kanji.objects.all():
        svg_filename = get_svg_filename(kanji.character)
        svg_path = os.path.join(SVG_FOLDER, svg_filename)
        
        if os.path.exists(svg_path):
            # Store the relative path to the SVG
            kanji.stroke_order_svg = f"stroke_order_svgs/{svg_filename}"
            kanji.save()
            print(f"Linked SVG for {kanji.character} -> {svg_filename}")
        else:
            print(f"SVG not found for {kanji.character}")

if __name__ == "__main__":
    link_svgs_to_kanji()
