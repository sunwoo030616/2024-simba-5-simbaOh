# Generated by Django 4.2.13 on 2024-06-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("careers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Careerinfo",
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
                ("title", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=30)),
                ("place", models.CharField(max_length=10)),
                ("content", models.TextField()),
                ("deadline", models.CharField(max_length=20)),
                ("pub_date", models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name="Info",
        ),
    ]
