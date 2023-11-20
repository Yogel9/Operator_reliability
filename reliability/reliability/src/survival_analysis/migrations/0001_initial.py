# Generated by Django 4.0.3 on 2023-11-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(null=True, verbose_name='Момент времени')),
                ('surviving_obj', models.IntegerField(null=True, verbose_name='Число объектов, доживающих до t')),
                ('failed_obj', models.IntegerField(null=True, verbose_name='Число объектов, для которых произошёл исход')),
                ('probability', models.FloatField(null=True, verbose_name='Вероятность исхода')),
            ],
            options={
                'verbose_name': 'Техническое оборудование',
                'verbose_name_plural': 'Техническое оборудование',
            },
        ),
    ]
