# Generated by Django 5.0.6 on 2024-07-04 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('campaign', '0028_alter_campaignemployee_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignImpersonationToken',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('token', models.TextField(db_index=True, unique=True)),
                ('valid_until_epoch_seconds', models.BigIntegerField()),
                ('used', models.BooleanField(default=False)),
                (
                    'campaign',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='campaign.campaign',
                    ),
                ),
                (
                    'campaign_employee',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='campaign.campaignemployee',
                    ),
                ),
                (
                    'employee_group_campaign',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='campaign.employeegroupcampaign',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
