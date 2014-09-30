# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0004_remove_company_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
