# Generated by Django 5.1.1 on 2024-09-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_category_image_departments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
