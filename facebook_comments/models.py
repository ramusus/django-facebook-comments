# -*- coding: utf-8 -*-
import logging
import re

from django.db import models
from facebook_api.mixins import OwnerableModelMixin, AuthorableModelMixin, LikableModelMixin
from facebook_api.models import FacebookGraphIDModel, FacebookGraphManager

log = logging.getLogger('facebook_comments')


class Comment(OwnerableModelMixin, AuthorableModelMixin, LikableModelMixin, FacebookGraphIDModel):

    message = models.TextField(help_text='The message')
    created_time = models.DateTimeField(help_text='The time the comment was initially published', db_index=True)

    can_remove = models.BooleanField(default=False)
    user_likes = models.BooleanField(default=False)

    objects = models.Manager()
    remote = FacebookGraphManager()

    class Meta:
        verbose_name = 'Facebook comment'
        verbose_name_plural = 'Facebook comments'

    @property
    def slug(self):
        # TODO: doesn't work with new ids like {PAGE_ID}:{POST_ID}:63_5258666
        # for example in post 147863265269488_588392457883231/comments
        comment_id = self.graph_id.split('_')[-1] if self.graph_id.count(':') != 2 else ''
        return '%s?comment_id=%s' % (self.owner.slug, comment_id)

    def parse(self, response):

        # don't touch graph_id like {PAGE_ID}:{POST_ID}:63_5258666
        if response['id'].count(':') != 2:
            # transform graph_id -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
            if response['id'].count('_') == 0:
                # group posts comments {COMMENT_ID} -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
                response['id'] = '_'.join([self.owner.graph_id, response['id']])
            elif response['id'].count('_') == 1:
                # page posts comments {POST_ID}_{COMMENT_ID} -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
                response['id'] = re.sub(r'^\d+', str(self.owner.graph_id), response['id'])

        super(Comment, self).parse(response)
