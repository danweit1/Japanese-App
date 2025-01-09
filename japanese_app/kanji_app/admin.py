from django.contrib import admin
from .models import Kanji

@admin.register(Kanji)
class KanjiAdmin(admin.ModelAdmin):
    list_display = ('character', 'jlpt_level', 'strokes')
    search_fields = ('character', 'onyomi', 'kunyomi', 'meaning')
