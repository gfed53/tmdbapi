import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from .models import CachedList
from django.utils import timezone

from .config import *

import tmdbsimple as tmdb
tmdb.API_KEY = API_KEY

mock_data = {}
mock_data['name'] = 'GoodFellas'
mock_data['year'] = 1990

def index(request):
  return HttpResponse('Hello World.')

def get_movie(request):
  return JsonResponse(mock_data)

def get_movies(request):
  # Mock
  json_data = json.loads(request.body)
  print('json_data',json_data)
  params = json_data['params']

  my_kwargs = {}

  if 'genres' in params:
    genres = '|'.join(str(x) for x in params['genres'])
    my_kwargs['with_genres'] = genres
    print('genres',genres)

  if 'dateFrom' in params:
    dateFrom = params['dateFrom']
    dateFromFormatted = dateFrom + '-01-01'
    my_kwargs['primary_release_date_gte'] = dateFromFormatted
    print('dateFromFormatted',dateFromFormatted)

  if 'dateTo' in params:
    dateTo = str(int(params['dateTo']) + 1)
    dateToFormatted = dateTo + '-01-01'
    my_kwargs['primary_release_date_lte'] = dateToFormatted
    print('dateToFormatted',dateToFormatted)

  print('my_kwargs',my_kwargs)

  discover = tmdb.Discover()
  response_data = discover.movie(**my_kwargs)

  return JsonResponse({'tmdb_results': response_data})

def get_movie_genres(request):
  genre = tmdb.Genres()

  # Check if there is a CacheList entry where name='genres' here
  

  response_data = genre.movie_list()

  # Basic implementation - create an entry into the CacheList model (after every API call while we're testing this out)


  # response_data_str = str(response_data)
  # cl = CachedList(
  #   name='genres',
  #   list_data=response_data_str,
  #   date_updated=timezone.now()
  # )

  # cl.save()



  return JsonResponse(response_data)

