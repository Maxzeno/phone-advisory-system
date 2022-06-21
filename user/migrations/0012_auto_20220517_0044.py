# Generated by Django 3.0.8 on 2022-05-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20220517_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phones',
            name='price',
        ),
        migrations.AddField(
            model_name='phones',
            name='price_min',
            field=models.FloatField(blank=True, default=100),
            preserve_default=False,
        ),
    ]