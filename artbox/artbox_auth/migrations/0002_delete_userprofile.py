# Generated by Django 3.1.4 on 2020-12-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0007_remove_art_user'),
        ('artbox_auth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
