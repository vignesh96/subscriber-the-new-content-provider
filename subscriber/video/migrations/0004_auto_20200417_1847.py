# Generated by Django 3.0.5 on 2020-04-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_upload_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.ImageField(upload_to='videos'),
        ),
    ]
