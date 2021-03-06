import base64
import html
import logging
import os
import romkan
import urllib

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery

from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kanjis.models import Kanji
from kanjis.serializers import KanjiSerializer

from kanjis.pdf.pdf_utils import generate_pdf

logger = logging.getLogger(__name__)


class KanjiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Readonly viewset for kanjis.
    """
    serializer_class = KanjiSerializer

    def get_queryset(self):
        queryset = Kanji.objects.all()
        search = self.request.query_params.get('q', None)
        jlpt = self.request.query_params.get('jlpt', None)
        if search:
            vector = SearchVector(
                'meanings', 'kun_readings', 'on_readings', 'kanji')
            search = SearchQuery(search)
            search_matcher = SearchRank(vector, search)
            queryset = Kanji.objects.annotate(
                matches=search_matcher
            ).filter(matches__gte=0.03).order_by('-matches', 'jlpt', 'stroke_count')

        if jlpt:
            queryset = queryset.filter(jlpt=jlpt)

        return queryset


@api_view(['GET'])
def romaji_to_kana(request):
    """
    Converts romaji in either katakana or hiragana.
    """
    word = request.query_params.get('word', '')[0:1000]
    return Response({'hiragana': romkan.to_hiragana(word), 'katakana': romkan.to_katakana(word)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def kanji_order(request):
    """
    Searchs for a svg kanji image and retrieve it or 404.
    """
    try:
        kanji = request.query_params.get('kanji', '')[0:10]
        kanji = html.unescape(kanji)
        if not kanji:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        code = '%05x' % ord(kanji)

        try:
            with open(os.path.join(settings.BASE_DIR, 'kanjis/kanjivg/kanji/{}.svg'.format(code)), 'rb') as kvg:
                kanji_b64 = base64.b64encode(kvg.read()).decode('utf-8')
                return Response({'svg': 'data:image/svg+xml;base64,{}'.format(kanji_b64)}, status=status.HTTP_200_OK)
        except FileNotFoundError as e:
            logger.error(e)
            return Response({'error': 'Kanji not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(e)
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def kanji_pdf(request):
    """
    Searchs for kanji pdf or generate one.
    """
    try:
        kanji_id = request.query_params.get('kanji_id', '')[0:10]
        try:
            kanji = Kanji.objects.get(pk=kanji_id)
        except Kanji.DoesNotExist:
            logger.error(e)
            return Response({'error': 'Kanji not found'}, status=status.HTTP_404_NOT_FOUND)

        code = '%05x' % ord(kanji.kanji)
        if not os.path.isfile(settings.MEDIA_ROOT + code + '.pdf'):
            generate_pdf(code, kanji)
        return Response({'url': '{}{}{}.pdf'.format(request.build_absolute_uri('/')[:-1], settings.MEDIA_URL, code)}, status=status.HTTP_200_OK)
    except urllib.error.URLError as e: 
        logger.error(e)
        return Response({'error': 'Kanji not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
