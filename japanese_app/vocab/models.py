
from django.db import models

class Vocab(models.Model):
    original = models.CharField(max_length=255, default="No value provided")
    furigana = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.TextField(default="No meaning provided")
    jlpt_level = models.CharField(max_length=10, default="N5")

    def __str__(self):
        return f"{self.original} ({self.jlpt_level})"
