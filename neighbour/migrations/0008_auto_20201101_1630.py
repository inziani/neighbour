# Generated by Django 3.1.2 on 2020-11-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_type',
            field=models.CharField(choices=[('PLUMBER', 'Plumber'), ('HAIR_SALON', 'Hair_Salon'), ('SHOP', 'Shop'), ('GYM', 'Gym'), ('GROCERY', 'Grocery'), ('CAPENTER', 'Capenter'), ('BUTCHERY', 'Butchery'), ('POLICE', 'Police'), ('HEALTH CENTRE', 'Health Center')], default='Business', max_length=255),
        ),
    ]
