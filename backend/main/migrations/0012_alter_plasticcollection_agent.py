# Generated by Django 5.1.2 on 2024-10-29 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_notification_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasticcollection',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent', to='main.userprofile'),
        ),
    ]
