# Generated by Django 3.0.5 on 2020-04-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20200417_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]