# Generated by Django 4.1 on 2022-08-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_juegos', '0007_juegos_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]
