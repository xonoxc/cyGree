# Generated by Django 5.1.2 on 2024-10-30 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_plasticcollection_agent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reward',
            unique_together={('user', 'reward')},
        ),
    ]
