# Any helper functions used within get_movie_genres view.


def getKwargs(params):
  """Takes params fetched from front end and returns kwargs object, properly formatted, to be used in API call"""
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

  # print('my_kwargs in helper',my_kwargs)

  return my_kwargs
