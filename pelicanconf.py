#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jared Andrews'
SITENAME = u'Jared Andrews'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'Unorganized'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

READERS = {"html": None}

THEME = 'theme'
STATIC_PATHS = ['images', 'making-this-site-rendered', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors', 'category_meta']

CURRENT_LOCATION = 'Pinellas County, Florida'
