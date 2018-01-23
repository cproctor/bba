#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BB&A Teaching Team'
SITENAME = 'Beyond Bits & Atoms'
SITEURL = ''
SITESUBTITLE = "Stanford EDUC 211 & 236 / CS 402 & 402L" 
OUTPUT_PATH = "output_local"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = 'themes/notmyidea'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images', 'resources']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

MENUITEMS = [
    ('Piazza', 'https://piazza.com/stanford/winter2018/educ211cs402l/home')

]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables': {}
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
