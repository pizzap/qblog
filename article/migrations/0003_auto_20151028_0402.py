# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151028_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256, verbose_name=b'\xe6\x8a\x95\xe7\xa8\xbf\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab'),
        ),
    ]
