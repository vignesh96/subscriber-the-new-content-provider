# Generated by Django 3.0.5 on 2020-04-16 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='video',
        ),
    ]
