from rest_framework import serializers
from .models import Kanji

class KanjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanji
        fields = "__all__"  # Include all fields in the API response
