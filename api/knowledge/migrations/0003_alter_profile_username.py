# Generated by Django 4.2.3 on 2023-07-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
