# Generated by Django 3.2.7 on 2021-09-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.CharField(default='', max_length=200),
        ),
    ]
