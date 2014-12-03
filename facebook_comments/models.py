# -*- coding: utf-8 -*-
import logging
import re

from django.db import models
from facebook_api.mixins import OwnerableModelMixin, AuthorableModelMixin, LikableModelMixin, ShareableModelMixin
from facebook_api.models import FacebookGraphStrPKModel, FacebookGraphManager

log = logging.getLogger('facebook_comments')


class Comment(OwnerableModelMixin, AuthorableModelMixin, LikableModelMixin, FacebookGraphStrPKModel):

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
        return '%s?comment_id=%s' % (self.owner.slug, self.graph_id.split('_')[-1])

    def parse(self, response):

        # transform graph_id from -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
        if response['id'].count('_') == 0:
            # group posts comments {COMMENT_ID} -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
            response['id'] = '_'.join([self.owner.graph_id, response['id']])
        elif response['id'].count('_') == 1:
            # page posts comments {POST_ID}_{COMMENT_ID} -> {PAGE_ID}_{POST_ID}_{COMMENT_ID}
            response['id'] = re.sub(r'^\d+', str(self.owner.graph_id), response['id'])

        super(Comment, self).parse(response)
