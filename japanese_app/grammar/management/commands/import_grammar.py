from django.core.management.base import BaseCommand
import csv
from grammar.models import Grammar


class Command(BaseCommand):
    help = "Import grammar points from a CSV file into the database"

    def handle(self, *args, **kwargs):
        # Path to the CSV file
        csv_file_path = "C:/Kanji/JLPT Grammar.csv"  # Update this path if needed

        try:
            with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=["level", "id", "grammar_point", "romaji", "meaning"])
                next(reader)  # Skip the header row if present

                for row in reader:
                    jlpt_level = row["level"].strip()
                    grammar_point = row["grammar_point"].strip()
                    romaji = row["romaji"].strip()
                    meaning = row["meaning"].strip()

                    # Skip rows with missing essential fields
                    if not grammar_point or not jlpt_level:
                        self.stderr.write("Skipping blank or incomplete entry")
                        continue

                    Grammar.objects.update_or_create(
                        grammar_point=grammar_point,
                        defaults={
                            "jlpt_level": jlpt_level,
                            "romaji": romaji,
                            "meaning": meaning,
                        }
                    )
                    self.stdout.write(f"Added/Updated grammar: {grammar_point} (JLPT {jlpt_level})")
        except FileNotFoundError:
            self.stderr.write(f"Error: File not found at {csv_file_path}")
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")

        self.stdout.write("Grammar data imported successfully!")
