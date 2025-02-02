# Generated by Django 5.1.1 on 2024-11-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0036_about_team_members_alter_delivery_delivery_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_percentage', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('banner', models.ImageField(upload_to='Offer')),
                ('products', models.ManyToManyField(related_name='special_offers', to='Main.product')),
            ],
        ),
    ]
