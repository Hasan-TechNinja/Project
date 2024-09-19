# Generated by Django 5.1.1 on 2024-09-18 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Hasan', max_length=100, null=True)),
                ('title', models.CharField(blank=True, default='This is the default, title change it in profile', max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='img/default.webp', null=True, upload_to='Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]