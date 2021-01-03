from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quiz import views

router = DefaultRouter()
router.register(r'decks', views.DeckViewSet)
router.register(r'flashcards', views.FlashcardViewSet)
router.register(r'quiz', views.QuizViewSet)
