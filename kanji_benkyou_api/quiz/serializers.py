from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from quiz.models import Deck, Flashcard, Quiz


class DeckSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Deck
        fields = '__all__' 


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
