# Generated by Django 3.2.7 on 2021-10-01 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name': 'Inquiry', 'verbose_name_plural': 'Inquiries'},
        ),
    ]
