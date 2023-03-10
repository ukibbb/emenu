# Generated by Django 4.1.7 on 2023-03-01 10:03

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "preparation_time",
                    models.TimeField(help_text="In minutes HH:mm:ss format"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_vegetarian", models.BooleanField(default=False)),
            ],
        ),
    ]
