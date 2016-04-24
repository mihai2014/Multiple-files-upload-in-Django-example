# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
