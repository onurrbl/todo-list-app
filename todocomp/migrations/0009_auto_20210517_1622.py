# Generated by Django 3.1.7 on 2021-05-17 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todocomp', '0008_auto_20210515_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user_session_fkey',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
    ]