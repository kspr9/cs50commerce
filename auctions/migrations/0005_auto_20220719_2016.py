# Generated by Django 3.0 on 2022-07-19 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20220719_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userswatchlist',
            name='listing_in_watchlist',
        ),
        migrations.AddField(
            model_name='userswatchlist',
            name='listing_in_watchlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
    ]
