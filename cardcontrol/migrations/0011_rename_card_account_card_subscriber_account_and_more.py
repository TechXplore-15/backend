# Generated by Django 5.1.6 on 2025-02-22 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardcontrol", "0010_card_is_subscribe_card_pay_day"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="card",
            old_name="card_account",
            new_name="subscriber_account",
        ),
        migrations.RenameField(
            model_name="card",
            old_name="card_name",
            new_name="subscriber_name",
        ),
        migrations.CreateModel(
            name="Transactions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "debit_account",
                    models.CharField(max_length=255, verbose_name="debit_account"),
                ),
                (
                    "credit_account",
                    models.CharField(max_length=255, verbose_name="credit_account"),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="created"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]
