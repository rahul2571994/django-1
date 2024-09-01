# Generated by Django 5.0.6 on 2024-08-11 15:32

from django.db import migrations

import lib.storage


class Migration(migrations.Migration):
    dependencies = [
        ('campaign', '0038_fix_order_status_cancelled_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='login_page_image',
            field=lib.storage.RandomNameImageField(
                blank=True,
                null=True,
                upload_to=lib.storage.RandomNameImageField._generate_random_file_name,
            ),
        ),
        migrations.AddField(
            model_name='campaign',
            name='login_page_mobile_image',
            field=lib.storage.RandomNameImageField(
                blank=True,
                null=True,
                upload_to=lib.storage.RandomNameImageField._generate_random_file_name,
            ),
        ),
    ]
