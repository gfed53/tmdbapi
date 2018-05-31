from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('get-movie/', views.get_movie, name='get-movie')
]