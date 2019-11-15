# Generated by Django 2.2.6 on 2019-11-15 15:11

import django.contrib.postgres.fields.jsonb
import django.core.files.storage
from django.db import migrations, models
import signals.apps.reporting.models.mixin


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export_parameters', django.contrib.postgres.fields.jsonb.JSONField(validators=[signals.apps.reporting.models.mixin.validate_parameters])),
                ('created_by', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_file', models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/dwh_media'), upload_to='category_exports/%Y')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='horecacsvexport',
            options={'ordering': ('-isoyear', '-isoweek', '-created_at')},
        ),
    ]
