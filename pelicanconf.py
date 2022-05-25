import os
import sys
from datetime import date

AUTHOR = 'Jack Tarricone'
SITENAME = 'Jack Tarricone'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UNR Graduate Program of Hydrologic Sciences', 'https://www.unr.edu/hydrologic-sciences'),
         ('Compututational Mountain Studies Lab', 'https://www.computationalmountainstudies.com/'),
         ('NASA SnowEx Campaign', 'https://snow.nasa.gov/campaigns/snowex'))

DEFAULT_PAGINATION = 5

# Theme
THEME = 'MinimalXY'

# Theme customizations
MINIMALXY_FAVICON = 'images/favicon.png'
MINIMALXY_START_YEAR = 2021
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = 'My name is Jack Tarricone. I’m a Ph.D. student in the [Computational Mountain Studies Lab](https://www.computationalmountainstudies.com/){:target="_blank"}, in the [Graduate Program of Hydrologic Sciences](https://www.unr.edu/hydrologic-sciences){:target="_blank"}, at the University of Nevada, Reno. My research focuses on optimizing and utilizing remote sensing techniques to estimate snowpack and surface water properties and fluxes at various space and time scales. I’m currently funded by the [NASA SnowEx](https://snow.nasa.gov/campaigns/snowex){:target="_blank"} campaign, a nationwide effort to advance our understanding of snow remote sensing. I received my B.A. *magna cum laude* in Geography from the University of Colorado, Boulder.'
AUTHOR_DESCRIPTION = ''
AUTHOR_AVATAR = '/images/avatar_small.jpeg'
AUTHOR_WEB = 'jacktarricone.github.io'


# Social
SOCIAL = (
    ('github', 'https://github.com/jacktarricone'),
    ('twitter', 'https://twitter.com/jack_tarricone'),
    ('linkedin', 'https://www.linkedin.com/in/jack-tarricone-b5170b109/'),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
