from django.contrib import admin
from .models import Grammar

@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('grammar_point', 'jlpt_level', 'romaji', 'meaning')
    search_fields = ('grammar_point', 'jlpt_level')
