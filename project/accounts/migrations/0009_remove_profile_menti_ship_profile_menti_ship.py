# Generated by Django 5.0.3 on 2024-06-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_menti_ship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='menti_ship',
        ),
        migrations.AddField(
            model_name='profile',
            name='menti_ship',
            field=models.ManyToManyField(related_name='mentor_ship', to='accounts.profile'),
        ),
    ]
