# Generated by Django 4.1.5 on 2023-02-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0009_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('confirmed', 'confirmed'), ('complete', 'complete')], default='open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
    ]
