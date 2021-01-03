from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated

from quiz.models import Deck, Flashcard, Quiz
from quiz.serializers import DeckSerializer, FlashcardSerializer, QuizSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """
    Viewset for decks.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class FlashcardViewSet(viewsets.ModelViewSet):
    """
    Viewset for flashcards.
    """
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class QuizViewSet(viewsets.ModelViewSet):
    """
    Viewset for quiz.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
