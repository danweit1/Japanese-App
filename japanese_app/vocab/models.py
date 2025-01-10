from django.db import models

class Vocab(models.Model):
    word = models.CharField(max_length=255, unique=True)
    furigana = models.CharField(max_length=255, blank=True, null=True)
    english = models.TextField(blank=True, null=True)
    jlpt_level = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.word} ({self.jlpt_level})"
