# Generated by Django 3.0.8 on 2022-06-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
