# Generated by Django 3.2.7 on 2021-11-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaport',
            name='to',
        ),
    ]