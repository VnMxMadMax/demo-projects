# Generated by Django 5.2.1 on 2025-05-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
