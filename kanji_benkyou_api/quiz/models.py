from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Deck(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE)
    kanji = models.JSONField(null=False, blank=False)
    elastic_id = models.CharField(max_length=100, null=False, blank=False)


class Quiz(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    max_score = models.IntegerField(null=False)
