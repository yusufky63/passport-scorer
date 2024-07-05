# Generated by Django 4.2.6 on 2024-06-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ceramic_cache", "0020_alter_ceramiccache_compose_db_save_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ceramiccache",
            name="expiration_date",
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="ceramiccache",
            name="issuance_date",
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]