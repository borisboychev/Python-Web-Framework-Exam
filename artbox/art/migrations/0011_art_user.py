# Generated by Django 3.1.4 on 2020-12-12 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201212_1459'),
        ('art', '0010_auto_20201211_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
            preserve_default=False,
        ),
    ]