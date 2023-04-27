# Generated by Django 4.1.7 on 2023-04-26 19:12

import apps.base.fields
import django.core.validators
import django.db.models.deletion
from django.core.management import call_command
from django.db import migrations, models


def load_fixtures(apps, schema_editor):
    call_command(
        'loaddata',
        'apps/external_payments/fixtures/services.json',
        verbosity=0,
    )
    call_command(
        'loaddata',
        'apps/external_payments/fixtures/yookassa_commissions.json',
        verbosity=0,
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('payment_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentService',
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
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCommission',
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
                ('payment_type', models.CharField(max_length=50, verbose_name='type_of_payment')),
                (
                    'commission',
                    apps.base.fields.CommissionField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Should be positive value',
                            ),
                            django.core.validators.MaxValueValidator(
                                100,
                                message='Should be not greater than 100',
                            ),
                        ],
                    ),
                ),
                (
                    'payment_service_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='external_payments.paymentservice',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='BalanceServiceMap',
            fields=[
                (
                    'payment_id',
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'balance_change_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='payment_accounts.balancechange',
                    ),
                ),
                (
                    'service_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='external_payments.paymentservice',
                    ),
                ),
            ],
        ),
        migrations.RunPython(load_fixtures),
    ]