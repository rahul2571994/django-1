# Generated by Django 5.0.3 on 2024-05-31 17:44

from django.db import migrations, models

import lib.phone_utils


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0014_alter_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                validators=[lib.phone_utils.validate_phone_number],
            ),
        ),
    ]
