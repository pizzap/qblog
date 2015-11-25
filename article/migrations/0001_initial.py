# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import redactor.fields
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading_img', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/%Y/%m/%d', verbose_name=b'\xe8\xa6\x8b\xe5\x87\xba\xe3\x81\x97\xe7\x94\xbb\xe5\x83\x8f')),
                ('summary', models.TextField(verbose_name=b'\xe8\xa6\x81\xe7\xb4\x84')),
                ('title', models.CharField(max_length=256, verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab')),
                ('content', redactor.fields.RedactorField(verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe5\x86\x85\xe5\xae\xb9')),
                ('status', models.CharField(default=b'private', max_length=16, verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe3\x82\xb9\xe3\x83\x86\xe3\x83\xbc\xe3\x82\xbf\xe3\x82\xb9', choices=[(b'publish', b'publish'), (b'pending', b'pending'), (b'draft', b'draft'), (b'private', b'private')])),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82')),
                ('author', models.ForeignKey(verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
    ]
