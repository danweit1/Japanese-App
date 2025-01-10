from django.http import JsonResponse
from django.views import View
from .models import Vocab

class VocabListView(View):
    def get(self, request):
        jlpt_level = request.GET.get('jlpt_level')
        if jlpt_level:
            vocab = Vocab.objects.filter(jlpt_level=jlpt_level)
        else:
            vocab = Vocab.objects.all()

        data = [{"original": v.original, "furigana": v.furigana, "meaning": v.meaning, "jlpt_level": v.jlpt_level} for v in vocab]
        return JsonResponse(data, safe=False)
