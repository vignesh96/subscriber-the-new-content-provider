# Generated by Django 3.0.5 on 2020-04-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20200417_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
