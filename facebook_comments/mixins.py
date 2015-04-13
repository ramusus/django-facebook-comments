# -*- coding: utf-8 -*-
import logging

from django.contrib.contenttypes.models import ContentType
from django.db import models
from facebook_api.api import api_call
from facebook_api.decorators import fetch_all, atomic

from .models import Comment
log = logging.getLogger('facebook_comments')


class CommentableModelMixin(models.Model):

    comments_count = models.PositiveIntegerField(null=True, help_text='The number of comments of this item')

    class Meta:
        abstract = True

#     def parse(self, response):
#         if 'comments' in response:
#             response['comments_count'] = len(response['comments']["data"])
#         super(CommentableModelMixin, self).parse(response)

    def update_count_and_get_comments(self, instances, *args, **kwargs):
        self.comments_count = instances.count()
        self.save()
        return instances.all()

    @atomic
    @fetch_all(return_all=update_count_and_get_comments, paging_next_arg_name='after')
    def fetch_comments(self, limit=100, filter='stream', summary=True, **kwargs):
        '''
        Retrieve and save all comments
        '''
        extra_fields = {
            'owner_content_type_id': ContentType.objects.get_for_model(self).pk,
            'owner_id': self.pk
        }
        ids = []
        response = api_call('%s/comments' %
                            self.graph_id, limit=limit, filter=filter, summary=int(summary), **kwargs)
        if response:
            log.debug('response objects count=%s, limit=%s, after=%s' %
                      (len(response['data']), limit, kwargs.get('after')))
            for resource in response['data']:
                instance = Comment.remote.get_or_create_from_resource(resource, extra_fields)
                ids += [instance.pk]

        return Comment.objects.filter(pk__in=ids), response
