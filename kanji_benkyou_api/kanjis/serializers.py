from rest_framework import serializers

from kanjis.models import Kanji

class KanjiSerializer(serializers.ModelSerializer):
    """
    Kanji serializer.
    """
    class Meta:
        model = Kanji
        fields = '__all__'
