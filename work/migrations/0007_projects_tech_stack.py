# Generated by Django 2.2.2 on 2019-08-16 20:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_auto_20190816_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='tech_stack',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=0, max_length=10), default=0, size=8),
        ),
    ]