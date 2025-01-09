from django.db import models

class Kanji(models.Model):
    character = models.CharField(max_length=1, unique=True)  # Single kanji character
    onyomi = models.CharField(max_length=100)               # On-yomi readings
    kunyomi = models.CharField(max_length=100)              # Kun-yomi readings
    jlpt_level = models.IntegerField()                      # JLPT level (1-5)
    strokes = models.IntegerField(null=True, blank=True)    # Stroke count
    meaning = models.TextField()                            # Meaning in English
    common_words = models.TextField(
        null=True, blank=True, help_text="Common words using this kanji"
    )
    stroke_order_svg = models.CharField(
    max_length=255, null=True, blank=True, help_text="Path to stroke order SVG"
    )

    def __str__(self):
        return self.character


