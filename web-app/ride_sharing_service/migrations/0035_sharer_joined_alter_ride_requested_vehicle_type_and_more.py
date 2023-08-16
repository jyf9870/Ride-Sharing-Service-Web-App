# Generated by Django 4.1.5 on 2023-02-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0034_remove_user_ride_id_sharer_ride_sharer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharer',
            name='joined',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle')], default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle')], max_length=64, null=True),
        ),
    ]
