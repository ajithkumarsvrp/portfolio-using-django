# Generated by Django 5.0.6 on 2024-05-30 14:23

import django.utils.timezone
import portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_profile_created_at_alter_profile_image_certification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certification',
            name='c_image',
            field=models.ImageField(blank=True, null=True, upload_to=portfolio.models.getFileName),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to=portfolio.models.getFileName),
        ),
    ]