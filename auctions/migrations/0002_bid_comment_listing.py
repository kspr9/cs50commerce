# Generated by Django 3.0 on 2022-07-18 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('starting_bid', models.PositiveIntegerField()),
                ('image_url', models.URLField(max_length=300)),
                ('listing_category', models.CharField(choices=[('CLOTHING', 'Clothing'), ('BROOMS', 'Brooms'), ('WANDS', 'Wands'), ('BOOKS', 'Magical Books'), ('ITEMS', 'Magical Items'), ('MYTHICAL', 'Mythical Items')], max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
