# Generated by Django 5.0.6 on 2024-08-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0024_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
