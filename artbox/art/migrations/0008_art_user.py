# Generated by Django 3.1.4 on 2020-12-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artbox_auth', '0003_userprofile'),
        ('art', '0007_remove_art_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='artbox_auth.userprofile'),
            preserve_default=False,
        ),
    ]
