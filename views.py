from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

import tmdbsimple as tmdb

mock_data = {}
mock_data['name'] = 'GoodFellas'
mock_data['year'] = 1990

def index(request):
  return HttpResponse('Hello World.')

def get_movie(request):
  return JsonResponse(mock_data)

