# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('interaction', models.PositiveIntegerField(verbose_name='interaction', default=0)),
                ('user', models.OneToOneField(verbose_name='user', related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('user',),
            },
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
