import csv
import pandas as pd
from django.core.management.base import BaseCommand
from kanji_app.models import Kanji


class Command(BaseCommand):
    help = "Link common vocabulary words to kanji based on JLPT levels"

    def handle(self, *args, **kwargs):
        CSV_FILE_PATH = r"C:\Kanji\jlpt_vocab.csv"  # Update with the correct path

        def get_words_by_kanji(csv_path):
            """
            Reads the JLPT vocab CSV and organizes words by kanji and level.
            Returns a dictionary mapping kanji to their associated words.
            """
            vocab_df = pd.read_csv(csv_path, encoding="utf-8")
            kanji_to_words_by_level = {}

            for _, row in vocab_df.iterrows():
                word = row["Original"]
                furigana = row["Furigana"]
                english = row["English"]

                # Clean up JLPT Level to ensure it matches expected format
                raw_level = row["JLPT Level"]
                if isinstance(raw_level, str) and raw_level.startswith("N") and raw_level[1:].isdigit():
                    jlpt_level = raw_level
                else:
                    print(f"Skipping invalid JLPT Level: {raw_level}")
                    continue

                formatted_word = f"{word} ({furigana}) - {english}"

                for kanji in word:
                    if "\u4e00" <= kanji <= "\u9faf":  # Check if character is kanji
                        if kanji not in kanji_to_words_by_level:
                            kanji_to_words_by_level[kanji] = {f"N{level}": [] for level in range(5, 0, -1)}
                        kanji_to_words_by_level[kanji][jlpt_level].append(formatted_word)

            print("Built kanji_to_words_by_level dictionary successfully.")
            return kanji_to_words_by_level

        def assign_common_words(kanji_char, kanji_level, kanji_to_words_by_level):
            """
            Assign up to 5 common words to a kanji by climbing JLPT levels.
            """
            common_words = []
            for level in [f"N{l}" for l in range(5, 0, -1)]:
                if kanji_char in kanji_to_words_by_level and level in kanji_to_words_by_level[kanji_char]:
                    words_at_level = kanji_to_words_by_level[kanji_char][level]
                    common_words.extend(words_at_level)
                    if len(common_words) >= 5:
                        return common_words[:5]
            return common_words[:5]

        def update_kanji_database(kanji_to_words_by_level):
            """
            Updates the Kanji model in the database with common words.
            """
            updated_kanji = 0
            for kanji in Kanji.objects.all():
                print(f"Processing kanji {kanji.character} (JLPT level: N{kanji.jlpt_level})...")
                common_words = assign_common_words(kanji.character, f"N{kanji.jlpt_level}", kanji_to_words_by_level)
                kanji.common_words = ", ".join(common_words)
                kanji.save()
                updated_kanji += 1
                print(f"Updated {kanji.character} with words: {common_words}")

            print(f"Updated common words for {updated_kanji} kanji.")

        print("Processing JLPT vocabulary CSV...")
        kanji_to_words_by_level = get_words_by_kanji(CSV_FILE_PATH)
        print("Updating database with common words by level...")
        update_kanji_database(kanji_to_words_by_level)
        print("Done!")
