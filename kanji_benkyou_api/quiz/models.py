from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Deck(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    @property
    def kanjis(self):
        return self.cards.values_list('char', flat=True)


class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE, related_name='cards')
    kanji = models.JSONField(null=False, blank=False)
    char = models.CharField(max_length=5, null=False, blank=False) # FIXME: Fix it to use the kanji inside the JSONField, check dev property


class Quiz(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    max_score = models.IntegerField(null=False)
