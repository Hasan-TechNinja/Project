# Generated by Django 5.1.1 on 2024-11-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0046_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='departments',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
