# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0005_delete_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('added_date', models.DateField(verbose_name='date added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
