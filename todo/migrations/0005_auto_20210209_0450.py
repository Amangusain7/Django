# Generated by Django 3.1.6 on 2021-02-09 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210209_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
    ]
