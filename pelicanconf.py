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

THEME = 'theme'
STATIC_PATHS = ['images']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors']
