# Generated by Django 3.0.8 on 2022-05-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20220517_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
