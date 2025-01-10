from django.http import JsonResponse
from django.views import View
from .models import Grammar

class GrammarListView(View):
    def get(self, request):
        jlpt_level = request.GET.get('jlpt_level')
        if jlpt_level:
            grammar = Grammar.objects.filter(jlpt_level=jlpt_level)
        else:
            grammar = Grammar.objects.all()

        data = [{"grammar_point": g.grammar_point, "meaning": g.meaning, "jlpt_level": g.jlpt_level} for g in grammar]
        return JsonResponse(data, safe=False)
