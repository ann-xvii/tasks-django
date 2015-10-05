# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20151004_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=100, help_text='Enter the project name')),
                ('color', models.CharField(verbose_name='color', max_length=7, help_text='Enter the hex color code, like #ccc or #cccccc', default='#fff', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')])),
                ('user', models.ForeignKey(verbose_name='user', to='taskmanager.Profile', related_name='projects')),
            ],
            options={
                'verbose_name': 'Project',
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
