from django.db import models
from django.contrib.auth.models import User

from rest_framework.serializers import ValidationError

from kanjis.models import Kanji


class Deck(models.Model):
    user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name='decks')
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    @property
    def kanji_list(self):
        return Flashcard.objects.filter(deck=self).values('kanji', 'kanji__kanji')

    def save(self, *args, **kwargs):
        """
        Limit decks per user.
        """
        if Deck.objects.filter(user=self.user).count() >= 10 and not self.id:
            raise ValidationError({'err': 'max_decks_per_user'})
        super(Deck, self).save(*args, **kwargs)


class Flashcard(models.Model):
    deck = models.ForeignKey(
        Deck, null=False, on_delete=models.CASCADE, related_name='cards')
    kanji = models.ForeignKey(
        Kanji, null=False, blank=False, on_delete=models.CASCADE)


class Quiz(models.Model):
    deck = models.ForeignKey(Deck, null=False, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    max_score = models.IntegerField(null=False)
