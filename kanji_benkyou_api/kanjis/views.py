import html
from django.shortcuts import render
from django.conf import settings

import romkan

from elasticsearch import Elasticsearch

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 


@api_view(['GET', 'POST'])
def search_kanji(request):
    """
    Search for kanjis on elasticsearch.
    """
    es = Elasticsearch([settings.ELASTIC_HOST])
    PAGE_SIZE = 50
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
