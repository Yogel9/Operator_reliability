# Generated by Django 4.0.3 on 2023-11-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0002_remove_millsparam_high_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='LipovParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HN', models.IntegerField(verbose_name='Первоначальное число ошибок в программе N')),
                ('m', models.IntegerField(verbose_name='Количество тестов m')),
                ('HS', models.IntegerField(verbose_name='Количество искусственно внесенных ошибок S')),
                ('n', models.IntegerField(verbose_name='Число найденных собственных ошибок n')),
                ('HV', models.IntegerField(verbose_name='Число обнаруженных к моменту оценки искусственных ошибок V')),
            ],
            options={
                'verbose_name': 'Липов параметр',
                'verbose_name_plural': 'Липов параметры',
            },
        ),
    ]
