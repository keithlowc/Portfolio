# Generated by Django 2.2.2 on 2019-08-17 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_auto_20190816_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='contact_message',
            new_name='message',
        ),
    ]
