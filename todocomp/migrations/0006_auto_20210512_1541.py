# Generated by Django 3.1.7 on 2021-05-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todocomp', '0005_auto_20210509_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_accomplished',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
