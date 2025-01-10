from django.contrib import admin
from .models import Vocab

@admin.register(Vocab)
class VocabAdmin(admin.ModelAdmin):
    list_display = ('word', 'furigana', 'english', 'jlpt_level')
    search_fields = ('word', 'jlpt_level')
