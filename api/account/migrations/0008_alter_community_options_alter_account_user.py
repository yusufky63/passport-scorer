# Generated by Django 4.1.3 on 2022-12-05 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0007_rename_communities_community"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="community",
            options={"verbose_name_plural": "Communities"},
        ),
        migrations.AlterField(
            model_name="account",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="account",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]