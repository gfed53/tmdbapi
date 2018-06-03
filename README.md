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

* Enjoy!