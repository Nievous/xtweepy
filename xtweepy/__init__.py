# -*- coding=utf-8 -*-
# Based on:
# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.
"""
Tweepy Twitter API library
"""
__version__ = '1.12'
__author__ = 'Joshua Roesslein (mod by Daniel M. S.)'
__license__ = 'MIT'

import sys
from tweepy.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, ModelFactory
from tweepy.error import TweepError
from xtweepy.xapi import XAPI
from tweepy.cache import Cache, MemoryCache, FileCache
from tweepy.auth import BasicAuthHandler, OAuthHandler
from tweepy.streaming import Stream, StreamListener
from tweepy.cursor import Cursor

reload(sys)
sys.setdefaultencoding('utf-8')

# Global, unauthenticated instance of API
api = XAPI()


def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level
