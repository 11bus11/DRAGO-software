# Generated by Django 4.1.7 on 2023-03-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragoSoftware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=254)),
                ('content', models.CharField(default='To be added', max_length=2000)),
                ('image', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
