import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

import tmdbsimple as tmdb
tmdb.API_KEY = ''

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
  # my_params = request.POST['params']
  my_params = {'data': json_data}




  # discover = tmdb.Discover
  # response_data = discover.movie(with_genres='')


  return JsonResponse({'received': my_params})

def get_movie_genres(request):
  genre = tmdb.Genres()
  response_data = genre.movie_list()
  return JsonResponse(response_data)

