# -*- coding=utf-8 -*-
import sys
from tweepy.api import API
from xbinder import bind_api
from tweepy.utils import list_to_csv

reload(sys)
sys.setdefaultencoding('utf-8')


class XAPI(API):

    def __init__(self, *args, **kwargs):
        super(XAPI, self).__init__(*args, **kwargs)

    """Search with 1.1 api"""
    newApiSearch = bind_api(
        path='/search/tweets.json',
        payload_type='json',
        allowed_param=['q', 'geocode', 'lang', 'locale', 'result_type', 'count',
                       'until', 'since_id', 'max_id', 'include_entities', 'callback']
    )

    """Get api rate limit with 1.1"""
    newApiRateLimit = bind_api(
        path='/application/rate_limit_status.json',
        payload_type='json',
        use_cache=False
    )

    """ Perform bulk look up of users from user ID or screenname """
    def lookup_users_new(self, user_ids=None, screen_names=None):
        return self._lookup_users_new(list_to_csv(user_ids), list_to_csv(screen_names))

    _lookup_users_new = bind_api(
        path='/users/lookup.json',
        payload_type='user', payload_list=True,
        allowed_param=['user_id', 'screen_name'],
    )

    """ statuses/retweets """
    newApiRetweets = bind_api(
        path='/statuses/retweets/{id}.json',
        payload_type='status', payload_list=True,
        allowed_param=['id', 'count'],
        require_auth=True
    )
