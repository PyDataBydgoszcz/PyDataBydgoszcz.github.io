AUTHOR = 'PyData Bydgoszcz'
SITENAME = 'PyData Bydgoszcz'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ["assets"]
THEME = "./themes/minimal-xy/"
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'meetup'
AUTHOR_HEADER="/assets/img/pydata_logo_big.jpg"
AUTHOR_AVATAR="/assets/img/pydata_logo.png"
AUTHOR_WEB=""

# Blogroll

# Social widget
SOCIAL = (
    ('meetup', 'https://www.meetup.com/PyData-Bydgoszcz/'),
    ('github', 'https://github.com/pydatabydgoszcz'),
    ('facebook', 'https://www.facebook.com/PyDataBydgoszcz/'),
    ('twitter', 'https://twitter.com/pydatabydgoszcz'),
    ('youtube', 'https://www.youtube.com/channel/UCe2iuKW4GLjR837xp-ERETQ'),
    ('email', 'mailto:pydata.bydgoszcz@gmail.com'),
    ('linkedin', 'https://www.linkedin.com/company/pydatabydgoszcz'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
