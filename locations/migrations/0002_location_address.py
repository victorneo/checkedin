# Generated by Django 3.0.1 on 2020-02-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
