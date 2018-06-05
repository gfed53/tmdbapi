import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

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

  if params['genres']:
    genres = ','.join(str(x) for x in params['genres'])
    print('genres',genres)

  if params['dateFrom']:
    dateFrom = params['dateFrom']
    dateFromFormatted = dateFrom + '-01-01'
    print('dateFromFormatted',dateFromFormatted)

  if(params['dateTo']):
    dateTo = str(int(params['dateTo']) + 1)
    dateToFormatted = dateTo + '-01-01'
    print('dateToFormatted',dateToFormatted)



  discover = tmdb.Discover()
  response_data = discover.movie(
    with_genres=genres,
    release_date_gte=dateFromFormatted,
    release_date_lte=dateToFormatted
    )


  return JsonResponse({'tmdb_results': response_data})

def get_movie_genres(request):
  genre = tmdb.Genres()
  response_data = genre.movie_list()
  return JsonResponse(response_data)

