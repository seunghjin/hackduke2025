# Generated by Django 5.0.6 on 2025-02-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tricen_backend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversation",
            name="needs_transfer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="conversation",
            name="transfer_reason",
            field=models.TextField(blank=True, null=True),
        ),
    ]
