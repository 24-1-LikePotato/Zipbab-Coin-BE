# Generated by Django 5.0.7 on 2024-07-25 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_subsribe',
            new_name='is_subscribe',
        ),
    ]
