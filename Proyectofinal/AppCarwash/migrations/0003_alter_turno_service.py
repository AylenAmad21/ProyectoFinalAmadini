# Generated by Django 4.2.6 on 2023-10-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarwash', '0002_turno_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='service',
            field=models.CharField(choices=[('1', 'Lavado Premium Basico'), ('2', 'Lavado Premium Plus'), ('3', 'Lavado Premium Deluxe'), ('4', 'Pulido Vehicular'), ('5', 'Pulido de Opticas'), ('6', 'Polarizado'), ('7', 'Wrapping Vehicular')], default=None, max_length=100, verbose_name='servicio'),
        ),
    ]
