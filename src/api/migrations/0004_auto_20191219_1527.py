# Generated by Django 2.0.5 on 2019-12-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191219_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='customers',
            field=models.ManyToManyField(blank=True, related_name='customers', to='api.Customer'),
        ),
    ]
