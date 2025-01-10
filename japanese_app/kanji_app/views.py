from django.http import JsonResponse
from django.views import View
from .models import Kanji

class KanjiListView(View):
    def get(self, request):
        jlpt_level = request.GET.get('jlpt_level')
        if jlpt_level:
            kanji = Kanji.objects.filter(jlpt_level=jlpt_level)
        else:
            kanji = Kanji.objects.all()

        data = [{"character": k.character, "meaning": k.meaning, "jlpt_level": k.jlpt_level} for k in kanji]
        return JsonResponse(data, safe=False)
