# Generated by Django 5.1.3 on 2024-11-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]