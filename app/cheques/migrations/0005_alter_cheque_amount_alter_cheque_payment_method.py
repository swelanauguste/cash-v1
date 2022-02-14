# Generated by Django 4.0.2 on 2022-02-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheques', '0004_alter_cheque_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheque',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cheque',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
