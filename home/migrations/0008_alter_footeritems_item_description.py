# Generated by Django 5.1.1 on 2024-10-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_footeritems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footeritems',
            name='item_description',
            field=models.TextField(),
        ),
    ]
