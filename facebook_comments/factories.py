# -*- coding: utf-8 -*-
from datetime import datetime
import random

from facebook_posts.factories import PostFactory
from facebook_users.factories import UserFactory
import factory
import models


class CommentFactory(factory.DjangoModelFactory):

    created_time = datetime.now()

    owner = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)
    graph_id = factory.LazyAttributeSequence(lambda o, n: '%s_%s' % (o.owner.graph_id, n))

    class Meta:
        model = models.Comment
