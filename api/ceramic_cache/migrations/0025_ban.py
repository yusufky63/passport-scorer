# Generated by Django 4.2.6 on 2024-11-23 00:00

from django.db import migrations, models

import account.models


class Migration(migrations.Migration):
    dependencies = [
        ("ceramic_cache", "0024_alter_revocation_proof_value"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ban",
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
                    "provider",
                    models.CharField(
                        blank=True, db_index=True, default="", max_length=256
                    ),
                ),
                (
                    "hash",
                    models.CharField(
                        blank=True, db_index=True, default="", max_length=100
                    ),
                ),
                (
                    "address",
                    account.models.EthAddressField(
                        blank=True, db_index=True, default="", max_length=42
                    ),
                ),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("reason", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "last_run_revoke_matching",
                    models.DateTimeField(
                        blank=True,
                        help_text="Last time revoke_matching_credentials was run",
                        null=True,
                    ),
                ),
            ],
        ),
    ]
