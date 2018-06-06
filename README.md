# TMDB Django App

This is a separate app used within a larger Django app which serves as a back end to a React movie-themed project. 

It currently is NOT tested to function on its own, having its own repo for version control purposes only. 

For deployment I plan on tying together the front and back end anyways, so this is really just for development purposes.

## So I can't actually use this?

Not sure if you'd want to, since it hardly does anything at this point. But if you're feeling bold, want to extend what I've started within your own app, and/or you're more comfortable with Django than I am, you can take the basic steps to integrate it into your own app.

* In your `settings.py`, add the app to your list of INSTALLED_APPS.

* Configure your root `urls.py` so that you can use the app.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    # Here
    path('tmdbapi/', include('tmdbapi.urls')),
]
```

* You would also need to allow CORS since your front end will most likely be at a different domain. You can install the [django-cors-headers](https://github.com/ottoyiu/django-cors-headers) package in your current environment:

`pip install django-cors-headers`

You can then go to your `settings.py` and add this to the bottom of your page:

```python
# All origins will be accepted
CORS_ORIGIN_ALLOW_ALL = True
```

You probably woudn't want to do this in production since it allows ANYONE to access your back end, so you can set certain domains to whitelist. The [documentation](https://github.com/ottoyiu/django-cors-headers) goes into further detail.

* Enjoy!