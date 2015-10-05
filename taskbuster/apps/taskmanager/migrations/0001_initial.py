# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('interaction', models.PositiveIntegerField(default=0, verbose_name='interaction')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile', verbose_name='user')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
