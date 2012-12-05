# -*- coding=utf-8 -*-
import sys
from tweepy.api import API
from xbinder import bind_api

reload(sys)
sys.setdefaultencoding('utf-8')


class XAPI(API):

    def __init__(self, *args, **kwargs):
        super(XAPI, self).__init__(*args, **kwargs)

    """Search with 1.1 api"""
    newApiSearch = bind_api(
        path = '/search/tweets.json',
        payload_type = 'json',
        allowed_param = ['q', 'geocode', 'lang', 'locale', 'result_type', 'count', 'until', 'since_id', 'max_id', 'include_entities', 'callback']
    )

    """Get api rate limit with 1.1"""
    newApiRateLimit = bind_api(
        path = '/application/rate_limit_status.json',
        payload_type = 'json',
        use_cache = False
    )
