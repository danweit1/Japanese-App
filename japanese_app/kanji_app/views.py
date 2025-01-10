from django.http import JsonResponse
from django.views import View
from .models import Kanji

class KanjiListView(View):
    """
    Handles GET requests to return a list of all Kanji.
    """
    def get(self, request):
        kanji = Kanji.objects.all()
        data = [{"character": k.character, "meaning": k.meaning, "jlpt_level": k.jlpt_level} for k in kanji]
        return JsonResponse(data, safe=False)
