# TMDB Django App

This is a separate app used within a larger Django app which serves as a back end to a React movie-themed project. 

It currently is NOT tested to function on its own, having its own repo for version control purposes only. 

For deployment I plan on tying together the front and back end, so note that this is just for development.

## Using this app

Though this hasn't been tested to work in other projects, if you're feeling bold and want to extend what I have within your own app, you can take the basic steps to attempt to integrate it into your own project.

* In your `settings.py`, add the app to your list of INSTALLED_APPS.

* Configure your root `urls.py` so that you can use the app.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    # Here
    path('tmdbapi/', include('tmdbapi.urls')),
]
```

* You would also need to allow CORS if your front end will be at a different domain. You can install the [django-cors-headers](https://github.com/ottoyiu/django-cors-headers) package in your current environment:

`pip install django-cors-headers`

You can then go to your `settings.py` and add this to the bottom of your page:

```python
# ALL origins will be accepted
CORS_ORIGIN_ALLOW_ALL = True
```

You probably woudn't want to do this in production since it allows ANYONE to access your back end, so you can set certain domains to whitelist. The [documentation](https://github.com/ottoyiu/django-cors-headers) goes into further detail.

* Since the app takes advantage of the [TMDB API](https://developers.themoviedb.org/3/getting-started/introduction), you will need an API key. Once you have a key, you can update `config.py`, setting `API_KEY` to the your acquired key.

You should now be up and running!