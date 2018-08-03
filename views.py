import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from .models import CachedList
from django.utils import timezone

from .config import *
import tmdbsimple as tmdb

from .helpers.get_movie_genres import *

tmdb.API_KEY = API_KEY

def get_movies(request):
  json_data = json.loads(request.body)
  print('json_data',json_data)
  params = json_data['params']
  my_kwargs = get_kwargs(params)

  print('my_kwarg length',len(my_kwargs))

  discover = tmdb.Discover()

  # if len(my_kwargs) > 3:
  #   # We need to do a 'modified' search
  #   print('do something else!')
  # else: 
    # response_data = discover.movie(**my_kwargs)
  response_data = modified_discover(my_kwargs)

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

