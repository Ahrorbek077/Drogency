# Generated by Django 5.0.7 on 2024-07-16 11:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_project_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='description'),
            preserve_default=False,
        ),
    ]