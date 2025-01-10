from django.core.management.base import BaseCommand
import csv
from vocab.models import Vocab


class Command(BaseCommand):
    help = "Import vocabulary data from a CSV file into the database"

    def handle(self, *args, **kwargs):
        # Path to the CSV file
        csv_file_path = "C:/Kanji/jlpt_vocab.csv"  # Update this path as necessary

        try:
            with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=["word", "furigana", "english", "jlpt_level"])
                next(reader)  # Skip the header row if present

                for row in reader:
                    word = row["word"].strip()
                    furigana = row["furigana"].strip()
                    english = row["english"].strip()
                    jlpt_level = row["jlpt_level"].strip()

                    # Skip rows with missing essential fields
                    if not word or not jlpt_level:
                        self.stderr.write("Skipping blank or incomplete entry")
                        continue

                    Vocab.objects.update_or_create(
                        word=word,
                        defaults={
                            "furigana": furigana,
                            "english": english,
                            "jlpt_level": jlpt_level,
                        },
                    )
                    self.stdout.write(f"Added/Updated vocabulary: {word} (JLPT {jlpt_level})")
        except FileNotFoundError:
            self.stderr.write(f"Error: File not found at {csv_file_path}")
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")

        self.stdout.write("Vocabulary data imported successfully!")
