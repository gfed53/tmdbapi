from django.urls import path

from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  # path('get-movie/', views.get_movie, name='get-movie'),
  path('get-movies/', views.get_movies, name='get-movies'),
  path('get-movie-genres', views.get_movie_genres, name='get-movie-genres')
]