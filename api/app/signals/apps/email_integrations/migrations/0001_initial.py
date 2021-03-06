# SPDX-License-Identifier: MPL-2.0
# Copyright (C) 2020 - 2021 Vereniging van Nederlandse Gemeenten, Gemeente Amsterdam
# Generated by Django 2.2.13 on 2020-12-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(
                    choices=[
                        ('signal_created', 'Send mail signal created'),
                        ('signal_status_changed_afgehandeld', 'Send mail signal handled'),
                        ('signal_status_changed_ingepland', 'Send mail signal scheduled'),
                        ('signal_status_changed_heropend', 'Send mail signal reopened'),
                        ('signal_status_changed_optional', 'Send mail optional')
                    ],
                    db_index=True,
                    max_length=100
                )),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(help_text='Het is mogelijk om Markdown en template variabelen te gebruiken')),
                ('created_by', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'E-mail template',
                'verbose_name_plural': 'E-mail templates',
            },
        ),
    ]
