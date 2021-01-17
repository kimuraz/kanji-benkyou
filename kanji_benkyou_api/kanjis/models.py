from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Kanji(models.Model):
    """
    Kanji data representation.
    """
    kanji = models.CharField(max_length=5, null=False, blank=False)

    grade = models.IntegerField(null=True)
    heisig_en = models.CharField(null=True, max_length=100)
    jlpt = models.IntegerField(null=True)
    kun_readings = ArrayField(models.CharField(
        blank=False, null=False, max_length=255), null=True)
    meanings = ArrayField(models.CharField(
        blank=False, null=False, max_length=255), null=True)
    name_readings = ArrayField(models.CharField(
        blank=False, null=False, max_length=255), null=True)
    on_readings = ArrayField(models.CharField(
        blank=False, null=False, max_length=255), null=True)
    stroke_count = models.IntegerField(null=True)
    unicode_code = models.CharField(max_length=5, null=False, blank=False)

    class Meta:
        ordering = ['jlpt', 'stroke_count', 'grade']
