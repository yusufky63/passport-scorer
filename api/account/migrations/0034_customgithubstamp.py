# Generated by Django 4.2.6 on 2024-08-30 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0033_accountapikey_analysis_rate_limit"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomGithubStamp",
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
                    "category",
                    models.CharField(
                        choices=[("repo", "Repository"), ("org", "Organization")],
                        max_length=4,
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        help_text="The repository (e.g. 'passportxyz/passport-scorer') or organization name (e.g. 'passportxyz')",
                        max_length=100,
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=7),
                ),
                (
                    "customization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="custom_github_stamps",
                        to="account.customization",
                    ),
                ),
            ],
        ),
    ]