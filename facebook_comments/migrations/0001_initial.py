# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration
class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'facebook_comments_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('graph_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=70)),
            ('owner_content_type', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='content_type_owners_comments', null=True, to=orm['contenttypes.ContentType'])),
            ('owner_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, db_index=True)),
            ('author_json', self.gf('annoying.fields.JSONField')(null=True)),
            ('author_content_type', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='content_type_authors_comments', null=True, to=orm['contenttypes.ContentType'])),
            ('author_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, db_index=True)),
            ('likes_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('can_remove', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_likes', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'facebook_comments', ['Comment'])

        # Adding M2M table for field likes_users on 'Comment'
        m2m_table_name = db.shorten_name(u'facebook_comments_comment_likes_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm[u'facebook_comments.comment'], null=False)),
            ('user', models.ForeignKey(orm[u'facebook_users.user'], null=False))
        ))
        db.add_column('facebook_comments_comment_likes_users', 'time_from',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, db_index=True),
                      keep_default=False)

        db.add_column('facebook_comments_comment_likes_users', 'time_to',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, db_index=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'facebook_comments_comment')

        # Removing M2M table for field likes_users on 'Comment'
        db.delete_table(db.shorten_name(u'facebook_comments_comment_likes_users'))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'facebook_comments.comment': {
            'Meta': {'object_name': 'Comment'},
            'author_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_authors_comments'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'author_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'author_json': ('annoying.fields.JSONField', [], {'null': 'True'}),
            'can_remove': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'graph_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'likes_users': ('m2m_history.fields.ManyToManyHistoryField', [], {'related_name': "'like_comments'", 'symmetrical': 'False', 'to': u"orm['facebook_users.User']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_owners_comments'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'owner_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'user_likes': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'facebook_users.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'cover': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'currency': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'devices': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'education': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'favorite_athletes': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'favorite_teams': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'graph_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'}),
            'hometown': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'interested_in': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'languages': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'location': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'payment_pricepoints': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'political': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quotes': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'relationship_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'security_settings': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'significant_other': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'third_party_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'video_upload_limits': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'work': ('annoying.fields.JSONField', [], {'max_length': '500', 'null': 'True'})
        }
    }

    complete_apps = ['facebook_comments']
