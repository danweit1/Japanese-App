from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Kanji
from .serializers import KanjiSerializer

class KanjiViewSet(viewsets.ModelViewSet):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jlpt_level', 'strokes', 'character']
