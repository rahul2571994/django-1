# Generated by Django 5.0.6 on 2024-07-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0023_alter_category_icon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, default=0),
        ),
    ]
