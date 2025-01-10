from django.db import models

class Grammar(models.Model):
    grammar_point = models.CharField(max_length=255, unique=True)
    jlpt_level = models.CharField(max_length=10)
    romaji = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.grammar_point} ({self.jlpt_level})"
