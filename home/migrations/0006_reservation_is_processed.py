# Generated by Django 5.1.1 on 2024-10-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]
