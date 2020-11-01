# Generated by Django 3.1.2 on 2020-11-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0004_neighbourhood_occupants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.CharField(choices=[('EAGLE COURT', 'Eagle'), ('PEACOCK COURT', 'Peacock'), ('SWAN COURT', 'Swan'), ('SWALLOW COURT', 'Swallow'), ('SEAGULL COURT', 'Seagull'), ('FLAMINGO COURT', 'Flamingo'), ('ROBIN COURT', 'Robin'), ('KINGFISHER COURT', 'Kingfisher')], default='Location', max_length=255),
        ),
    ]