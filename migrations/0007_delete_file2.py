# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20160423_1948'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File2',
        ),
    ]
