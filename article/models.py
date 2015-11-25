# -*- coding: utf-8 -*-

"""Article module."""
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from redactor.fields import RedactorField
from taggit.managers import TaggableManager

class Post(models.Model):
    """docstring for Post."""
    author = models.ForeignKey(User, verbose_name='投稿者')
    heading_img = ImageField('見出し画像', upload_to='uploads/%Y/%m/%d', max_length=100, height_field=None, width_field=None)
    summary = models.TextField('要約')
    title = models.CharField('投稿タイトル', max_length=256)
    content = RedactorField('投稿内容')
    STATUS_CHOICE = (
        ('publish', 'publish'),
        ('pending', 'pending'),
        ('draft', 'draft'),
        ('private', 'private'),
    )
    status = models.CharField('投稿ステータス', max_length=16, choices=STATUS_CHOICE, default='private')
    created_at = models.DateTimeField('作成日時', auto_now=True)
    updated_at = models.DateTimeField('更新日時', auto_now_add=True)
    tags = TaggableManager()
    def __unicode__(self, *args, **kwargs):
        return self.title