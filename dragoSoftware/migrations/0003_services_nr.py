# Generated by Django 3.2.16 on 2023-03-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragoSoftware', '0002_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='nr',
            field=models.IntegerField(default=0),
        ),
    ]
