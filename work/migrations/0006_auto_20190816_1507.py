# Generated by Django 2.2.2 on 2019-08-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20190815_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
