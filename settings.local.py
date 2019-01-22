#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path

SITENAME = 'Beyond Bits & Atoms'
SITEURL = str(Path(__file__).resolve().parent / "output_local")
SITESUBTITLE = "LOCAL" 
OUTPUT_PATH = "output_local"

# These settings tell Pelican to speed up build by only re-processing content which has changed. 
# See details in the Pelican documentation
LOAD_CONTENT_CACHE = True           # Use caching
CHECK_MODIFIED_METHOD = 'mtime'     # Use modified time to check whether content has changed
CACHE_CONTENT = True                # Save changes to the cache
CONTENT_CACHING_LAYER = 'generator' # Cache at the layer of generators (alt: 'reader')
WITH_FUTURE_DATES = False           # Incompatible with caching

# Base path of content
PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%a, %b %d'

DEFAULT_LANG = 'en'

THEME = 'themes/notmyidea'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images', 'resources']

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['filetime_from_git', 'replacer']

REPLACES = (
    ("TODO", '<span class="todo">TODO</span>'),
    ("READINGS_URL", "http://beyondbitsandatoms.org/readings")
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

MENUITEMS = [
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables': {}
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
