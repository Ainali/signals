# Generated by Django 2.1 on 2018-09-18 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0011_auto_20180918_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='department',
        ),
        migrations.RemoveField(
            model_name='category',
            name='main',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_cat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_cat_all',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_cat_all_prob',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_priority',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_prob',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_sub_all',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_sub_all_prob',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_sub_cat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='ml_sub_prob',
        ),
        migrations.RemoveField(
            model_name='category',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub',
        ),
        migrations.AddField(
            model_name='signal',
            name='sub_categories',
            field=models.ManyToManyField(through='signals.Category', to='signals.SubCategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='_signal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='category_assignments',
                                    to='signals.Signal'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='category_assignments',
                                    to='signals.SubCategory'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='code',
        ),
    ]
