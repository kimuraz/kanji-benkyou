from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kanjis import views

router = DefaultRouter()
router.register(r'kanjis', views.KanjiViewSet, basename='Kanji')
