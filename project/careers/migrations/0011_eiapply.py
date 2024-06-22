# Generated by Django 4.2.13 on 2024-06-23 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("careers", "0010_cpapply"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eiapply",
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
                ("application_date", models.DateTimeField(auto_now_add=True)),
                (
                    "eduinfo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="careers.eduinfo",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
