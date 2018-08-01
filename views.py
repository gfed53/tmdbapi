import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from .models import CachedList
from django.utils import timezone

from .config import *

import tmdbsimple as tmdb
tmdb.API_KEY = API_KEY

def get_movies(request):
  json_data = json.loads(request.body)
  print('json_data',json_data)
  params = json_data['params']

  # This is basically a list of options that will be passed to the request.
  my_kwargs = {}

  # We're looking into our params object passed in as part of our request body, and constructing our my_kwargs list based on what params exist on the params object. There may be a cleaner way to do this, though we have to parse the data within the params anyways so they have the proper, expected syntax.
  if 'genres' in params:
    genres = '|'.join(str(x) for x in params['genres'])
    my_kwargs['with_genres'] = genres
    # print('genres',genres)

  if 'dateFrom' in params:
    dateFrom = params['dateFrom']
    dateFromFormatted = dateFrom + '-01-01'
    my_kwargs['primary_release_date_gte'] = dateFromFormatted
    # print('dateFromFormatted',dateFromFormatted)

  if 'dateTo' in params:
    dateTo = str(int(params['dateTo']) + 1)
    dateToFormatted = dateTo + '-01-01'
    my_kwargs['primary_release_date_lte'] = dateToFormatted
    # print('dateToFormatted',dateToFormatted)
  
  # Default sort order
  sort_by_tup = ['popularity','desc']

  if 'orderType' in params:
    sort_by_tup[0] = params['orderType']

  if 'orderDirection' in params:
    sort_by_tup[1] = params['orderDirection']

  my_kwargs['sort_by'] = '.'.join(x for x in sort_by_tup)
  
  if 'page' in params:
    my_kwargs['page'] = params['page']
    # print('page',my_kwargs['page'])

  # print('my_kwargs',my_kwargs)

  discover = tmdb.Discover()
  response_data = discover.movie(**my_kwargs)

  return JsonResponse({'tmdb_results': response_data})

def get_movie_genres(request):
  genre = tmdb.Genres()

  # Check if there is a CacheList entry where name='genres' here
  # Soon we will also check if list is old and needs to be updated
  
  if CachedList.objects.filter(name='genres'):
    # print('genres exists',CachedList.objects.filter(name='genres'))
    cl = CachedList.objects.filter(name='genres')[0]
    response_data_str = cl.list_data
    # print('response_data_str',response_data_str)
    response_data = json.loads(response_data_str)

    return JsonResponse(response_data)
  else:
    response_data = genre.movie_list()

    # Basic implementation - create an entry into the CacheList model 

    response_data_str = json.dumps(response_data)

    cl = CachedList(
      name='genres',
      list_data=response_data_str,
      date_updated=timezone.now()
    )

    cl.save()

    return JsonResponse(response_data)

