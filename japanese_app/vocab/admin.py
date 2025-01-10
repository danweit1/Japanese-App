from django.contrib import admin
from .models import Vocab

@admin.register(Vocab)
class VocabAdmin(admin.ModelAdmin):
    list_display = ('original', 'furigana', 'meaning', 'jlpt_level')  # Update to match model fields
