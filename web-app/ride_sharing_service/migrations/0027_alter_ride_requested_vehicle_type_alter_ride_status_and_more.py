# Generated by Django 4.1.5 on 2023-02-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0026_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback'), ('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle'), ('Truck', 'Pickup Truck'), ('Convertible', 'Convertible')], default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Confirmed', 'Confirmed'), ('Open', 'Open')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback'), ('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle'), ('Truck', 'Pickup Truck'), ('Convertible', 'Convertible')], max_length=64, null=True),
        ),
    ]
