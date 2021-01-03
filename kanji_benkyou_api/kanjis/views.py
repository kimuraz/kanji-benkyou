from django.shortcuts import render
from django.conf import settings

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
        'query': {}
    }

    if request.method == 'POST':
        data = request.data
        search_param['query']['match'] = data
    elif request.method == 'GET':
        query = request.query_params.get('q', '')
        search_param['query']['query_string'] = {
            'query': query,
            'default_field': 'meanings',
        }

    results = es.search(index='kanjis', body=search_param, filter_path=['hits.hits.*']).get('hits', {'hits': []})['hits']

    if len(results) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({ 'results': results }, status=status.HTTP_200_OK)
