# Generated by Django 5.0.6 on 2024-07-02 10:54

from django.db import migrations, models

import campaign.models


class Migration(migrations.Migration):
    dependencies = [
        ('campaign', '0026_remove_cart_group_campaign_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeegroupcampaign',
            name='displayed_currency',
            field=models.CharField(
                choices=[('COINS', 'Coins'), ('CURRENCY', 'Currency')],
                default=campaign.models.EmployeeGroupCampaign.CurrencyTypeEnum[
                    'CURRENCY'
                ],
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name='employeegroupcampaign',
            name='product_selection_mode',
            field=models.CharField(
                choices=[('SINGLE', 'Single'), ('MULTIPLE', 'Multiple')],
                default=campaign.models.EmployeeGroupCampaign.ProductSelectionTypeEnum[
                    'SINGLE'
                ],
                max_length=32,
            ),
        ),
    ]
