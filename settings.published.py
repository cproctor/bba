#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'BB&A Teaching Team'
SITENAME = 'Beyond Bits & Atoms'
SITEURL = 'http://beyondbitsandatoms.org'
SITESUBTITLE = "Teachers College MSTU 5199 001 & 002" 
OUTPUT_PATH = "output_published"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'themes/notmyidea'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images', 'resources']

# Plugins
PLUGIN_PATHS = ['plugins', 'pelican-plugins']
PLUGINS = ['filetime_from_git', 'replacer', 'markdown_raw_reader']

REPLACES = (
    ("TODO", '<span class="todo">TODO</span>'),
    ("READINGS_URL", "http://beyondbitsandatoms.org/readings"),
    ("CANVAS_LECTURE_URL", "https://tc.instructure.com/courses/8886"),
    ("CANVAS_LAB_URL", "https://tc.instructure.com/courses/8887")
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
ARTICLE_ORDER_BY = lambda article: float(article.metadata.get('index', 1000))

MENUITEMS = [
    ('Piazza', 'https://piazza.com/class/jr73emlmjcftj')
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables': {}
    }
}

READERS = {
    "md": "markdown_raw_reader.MarkdownRawReader"
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
