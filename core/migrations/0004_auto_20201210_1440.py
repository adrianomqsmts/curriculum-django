# Generated by Django 3.1.4 on 2020-12-10 17:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201210_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)], verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)], verbose_name='Start'),
        ),
    ]