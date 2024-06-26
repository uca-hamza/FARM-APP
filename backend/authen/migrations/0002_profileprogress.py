# Generated by Django 4.2.1 on 2024-04-17 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileProgress",
            fields=[
                ("id_progress", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("temperature", models.FloatField()),
                ("pressure", models.FloatField()),
                ("food", models.FloatField()),
                ("medicine", models.FloatField()),
                ("gas", models.FloatField()),
                ("water", models.FloatField()),
                ("mortality", models.FloatField()),
                ("weight", models.FloatField()),
                (
                    "id_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
