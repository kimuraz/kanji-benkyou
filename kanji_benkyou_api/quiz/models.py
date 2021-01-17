from django.db import models
from django.contrib.auth.models import User

from kanjis.models import Kanji


class Deck(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


class Flashcard(models.Model):
    deck = models.ForeignKey(
        Deck, null=False, on_delete=models.CASCADE, related_name='cards')
    kanji = models.ForeignKey(
        Kanji, null=False, blank=False, on_delete=models.CASCADE)


class Quiz(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    max_score = models.IntegerField(null=False)
