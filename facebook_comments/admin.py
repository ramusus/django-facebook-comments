# -*- coding: utf-8 -*-
from django.contrib import admin
from facebook_api.admin import FacebookModelAdmin

from .models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('created_time', 'author', 'message', 'likes_count', 'like_users')
    readonly_fields = fields
    extra = False
    can_delete = False


class CommentAdmin(FacebookModelAdmin):
    list_display = ('author', 'created_time', 'message', 'likes_count')
    list_display_links = ('message',)
    search_fields = ('message',)

    def get_readonly_fields(self, *args, **kwargs):
        fields = super(CommentAdmin, self).get_readonly_fields(*args, **kwargs)
        return fields + ['like_users']


admin.site.register(Comment, CommentAdmin)
