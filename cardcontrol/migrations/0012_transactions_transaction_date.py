# Generated by Django 5.1.6 on 2025-02-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardcontrol", "0011_rename_card_account_card_subscriber_account_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="transaction_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="date"),
        ),
    ]
