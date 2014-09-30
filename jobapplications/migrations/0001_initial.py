# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
