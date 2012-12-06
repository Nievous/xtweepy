Extensión de tweepy para realizar búsquedas usando la api 1.1 de twitter.

Adicionalmente el resultado también entrega los headers (útil para revisar el límite actual de consultas).

Uso:

In [1]: import xtweepy

In [2]: secret = 'xxxxx'

In [3]: key = 'xxxxxxx'

In [4]: consumer_key = 'xxxxx'

In [5]: consumer_secret = 'xxxxx'

In [6]: auth = xtweepy.OAuthHandler(consumer_key, consumer_secret)

In [7]: auth.set_access_token(key, secret)

In [8]: newApi = xtweepy.XAPI(auth, api_root='/1.1')

In [9]: result, headers = newApi.newApiSearch("gatos")

In [10]: headers['x-rate-limit-remaining']
'179'

