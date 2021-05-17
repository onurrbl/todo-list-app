# Generated by Django 3.1.7 on 2021-05-15 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('todocomp', '0007_auto_20210514_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AddField(
            model_name='todo',
            name='user_session_fkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='sessions.session'),
        ),
    ]
