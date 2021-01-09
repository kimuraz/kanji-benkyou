import base64
import html
import logging
import os
import romkan

from django.shortcuts import render
from django.conf import settings

from elasticsearch import Elasticsearch

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

logger = logging.getLogger(__name__)

PAGE_SIZE = 50

@api_view(['GET', 'POST'])
def search_kanji(request):
    """
    Search for kanjis on elasticsearch.
    """
    es = Elasticsearch([settings.ELASTIC_HOST])
    page = request.query_params.get('page', '0') 
    search_param = {
        'from': PAGE_SIZE * (int(page) if page.isdecimal() else 0),
        'size': PAGE_SIZE,
        'sort': [
            '_score',
            'grade',
            { 'stroke_count': { 'order': 'asc' } },
            'jlpt',
        ],
        'query': {}
    }

    if request.method == 'POST':
        data = request.data
        search_param['query']['match'] = data
    elif request.method == 'GET':
        query = request.query_params.get('q', '')
        query = html.unescape(query)
        search_param['query']['query_string'] = {
            'query': query if query else '*',
        }

    results = es.search(index='kanjis', body=search_param, filter_path=['hits.total', 'hits.hits._id', 'hits.hits._source']).get('hits', {'hits': []})

    if len(results) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({ 'results': results.get('hits', []), 'total': results['total']['value'] }, status=status.HTTP_200_OK)

@api_view(['GET'])
def romaji_to_kana(request):
    """
    Converts romaji in either katakana or hiragana.
    """
    word = request.query_params.get('word', '')[0:1000]
    return Response({ 'hiragana': romkan.to_hiragana(word), 'katakana': romkan.to_katakana(word) }, status=status.HTTP_200_OK)


@api_view(['GET'])
def kanji_order(request):
    """
    Searchs for a svg kanji image and retrieve it or 404.
    """
    try:
        kanji = request.query_params.get('kanji', '')[0:10]
        kanji = html.unescape(kanji)
        if not kanji:
            return Response({}, status=status.HTP_400_BAD_REQUEST)
        code = '%05x' % ord(kanji)

        try:
            with open(os.path.join(settings.BASE_DIR, 'kanjis/kanjivg/kanji/{}.svg'.format(code)), 'rb') as kvg:
                kanji_b64 = base64.b64encode(kvg.read()).decode('utf-8')
                return Response({ 'svg': 'data:image/svg+xml;base64,{}'.format(kanji_b64) }, status=status.HTTP_200_OK)
        except FileNotFoundError as e:
            logger.error(e)
            return Response({ 'error': 'Kanji not found' }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(e)
        return Response({ 'error': str(e) }, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def kanji_by_jlpt(request):
    """
    Retrieve kanjis by JLPT level
    """
    es = Elasticsearch([settings.ELASTIC_HOST])
    page = request.query_params.get('page', '0') 
    jlpt = request.query_params.get('jlpt', '4')
    search_param = {
        'from': PAGE_SIZE * (int(page) if page.isdecimal() else 0),
        'size': PAGE_SIZE,
        'sort': [
            '_score',
            { 'stroke_count': { 'order': 'asc' } },
        ],
        'query': {
            'match': {
                'jlpt': (int(jlpt) if jlpt.isdecimal() else 4)
            }
        }
    }

    results = es.search(index='kanjis', body=search_param, filter_path=['hits.total', 'hits.hits._id', 'hits.hits._source']).get('hits', {'hits': []})

    if len(results) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({ 'results': results.get('hits', []), 'total': results['total']['value'] }, status=status.HTTP_200_OK)
