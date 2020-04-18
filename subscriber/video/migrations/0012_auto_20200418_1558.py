# Generated by Django 3.0.5 on 2020-04-18 10:28

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0011_auto_20200418_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(null=True, upload_to='videos', validators=[video.validators.validate_file_size]),
        ),
    ]
