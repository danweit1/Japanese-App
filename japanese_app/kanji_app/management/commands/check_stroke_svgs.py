import os
from django.core.management.base import BaseCommand
from kanji_app.models import Kanji

SVG_FOLDER = r"C:\Kanji\VG\kanjivg-master\kanji"  # Update with the actual path to your SVG folder

class Command(BaseCommand):
    help = "Verify and link stroke order SVG files for kanji"

    def handle(self, *args, **kwargs):
        missing_svgs = []
        updated_kanji = 0

        for kanji in Kanji.objects.all():
            svg_filename = f"{ord(kanji.character):05X}.svg"  # Unicode code point of the character
            svg_path = os.path.join(SVG_FOLDER, svg_filename)

            if os.path.exists(svg_path):
                kanji.stroke_order_svg = f"stroke_order_svgs/{svg_filename}"  # Update path relative to MEDIA_ROOT
                kanji.save()
                updated_kanji += 1
            else:
                missing_svgs.append(kanji.character)

        self.stdout.write(self.style.SUCCESS(f"Updated stroke order SVGs for {updated_kanji} kanji."))
        if missing_svgs:
            self.stdout.write(f"Missing SVG files for {len(missing_svgs)} kanji: {', '.join(missing_svgs)}")
