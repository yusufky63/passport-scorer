# Generated by Django 4.2.6 on 2024-01-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ceramic_cache", "0016_alter_ceramiccache_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ceramiccache",
            name="compose_db_save_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pending", "Pending"),
                    ("saved", "Saved"),
                    ("failed", "Failed"),
                ],
                default="",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="ceramiccache",
            name="compose_db_stream_id",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]