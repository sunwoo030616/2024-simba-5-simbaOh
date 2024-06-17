# Generated by Django 5.0.3 on 2024-06-17 14:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_phone', models.CharField(max_length=50)),
                ('user_birth', models.DateField()),
                ('user_major', models.CharField(blank=True, max_length=100)),
                ('user_profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user_enroll', models.CharField(blank=True, max_length=50)),
                ('updated_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]