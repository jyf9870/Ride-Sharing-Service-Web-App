# Generated by Django 4.1.5 on 2023-02-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0007_rename_arrival_date_ride_arrival_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='passenger_num',
            new_name='passenger_number',
        ),
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback'), ('Truck', 'Pickup Truck'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Sedan', 'Sedan'), ('SUV', 'Sport Utility Vehicle')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('complete', 'complete'), ('confirmed', 'confirmed')], default='open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback'), ('Truck', 'Pickup Truck'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Sedan', 'Sedan'), ('SUV', 'Sport Utility Vehicle')], max_length=64, null=True),
        ),
    ]
