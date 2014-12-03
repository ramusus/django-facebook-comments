# Django Facebook Graph API Comments

[![PyPI version](https://badge.fury.io/py/django-facebook-comments.png)](http://badge.fury.io/py/django-facebook-comments) [![Build Status](https://travis-ci.org/ramusus/django-facebook-comments.png?branch=master)](https://travis-ci.org/ramusus/django-facebook-comments) [![Coverage Status](https://coveralls.io/repos/ramusus/django-facebook-comments/badge.png?branch=master)](https://coveralls.io/r/ramusus/django-facebook-comments)

Application for interacting with Facebook Graph API Comments objects using Django model interface

## Installation

    pip install -e git+https://github.com/ramusus/django-facebook-comments.git#egg=django_facebook_comments

Add into `settings.py` lines:

    INSTALLED_APPS = (
        ...
        'oauth_tokens',
        'facebook_api',
        'facebook_users',
        'facebook_comments',
    )

    # oauth-tokens settings
    OAUTH_TOKENS_HISTORY = True                                        # to keep in DB expired access tokens
    OAUTH_TOKENS_FACEBOOK_CLIENT_ID = ''                               # application ID
    OAUTH_TOKENS_FACEBOOK_CLIENT_SECRET = ''                           # application secret key
    OAUTH_TOKENS_FACEBOOK_SCOPE = ['offline_access']                   # application scopes
    OAUTH_TOKENS_FACEBOOK_USERNAME = ''                                # user login
    OAUTH_TOKENS_FACEBOOK_PASSWORD = ''                                # user password

## Usage examples

### Fetch post comments

    >>> from facebook_posts.models import Post
    >>> post = Post.remote.fetch('19292868552_10150189643478553')
    >>> post.fetch_comments()
    [<Comment: Comment object>, <Comment: Comment object>, <Comment: Comment object>, '...(remaining elements truncated)...']
    >>> post.comments.count()
    82
    >>> post.comments.all()[0].__dict__
    Out[53]:
    {'_external_links_post_save': [],
     '_external_links_to_add': [],
     '_foreignkeys_post_save': [],
     '_state': <django.db.models.base.ModelState at 0xbfc51cc>,
     'author_content_type_id': 87,
     'author_id': 6447,
     'author_json': {u'id': u'767515690', u'name': u'Tim McKnight'},
     'can_remove': False,
     'created_time': datetime.datetime(2013, 3, 15, 5, 24, 46),
     'graph_id': u'19292868552_10150189643478553_25321001',
     'id': 3605,
     'likes_count': 0,
     'likes_real_count': 0,
     'message': u'test',
     'post_id': 4364,
     'user_likes': False}

Fetch all comments of post

    >>> post.fetch_comments(all=True)
    [<Comment: Comment object>, <Comment: Comment object>, <Comment: Comment object>, '...(remaining elements truncated)...']
    >>> page.wall_comments.count()
    610

### Fetch comment likes

    >>> from facebook_posts.models import Post, Comment
    >>> post = Post.remote.fetch('19292868552_10150189643478553')
    >>> comment = Comment.remote.fetch('19292868552_10150189643478553_16210808')
    >>> comment.likes_count # field with likes ammount transfered via API
    480
    >>> comment.likes_real_count # field with ammount of real likes connections
    0
    >>> comment.fetch_likes()
    [<User: Blondi Gjini>, <User: Kerem Aydoğan>, '...(remaining elements truncated)...']
    >>> comment.like_users.count()
    480
    >>> comment.likes_real_count
    480
