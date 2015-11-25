# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post
from django import forms
from redactor.widgets import RedactorEditor

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
           'short_text': RedactorEditor(),
        }
        exclude = ['created_at', 'updated_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm