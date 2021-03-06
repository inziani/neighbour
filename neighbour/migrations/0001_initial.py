# Generated by Django 3.1.2 on 2020-11-01 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('location', models.CharField(choices=[('EAGLE_COURT', 'Eagle'), ('PEACOCK_COURT', 'Peacock'), ('SWAN_COURT', 'Swan'), ('SWALLOW_COURT', 'Swallow'), ('SEAGULL_COURT', 'Seagull'), ('FLAMINGO', 'Flamingo'), ('ROBIN_COURT', 'Robin'), ('KINGFISHER_COURT', 'Kingfisher')], default='Location', max_length=255)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
