# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20151029_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='place',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
