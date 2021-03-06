# Generated by Django 3.1.4 on 2020-12-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201212_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='user_pictures')),
                ('username', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
            ],
        ),
    ]
