# Generated by Django 3.0.8 on 2022-05-10 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220509_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact us'},
        ),
        migrations.AlterModelOptions(
            name='faqs',
            options={'verbose_name': 'FAQ'},
        ),
        migrations.AlterModelOptions(
            name='favourite',
            options={'verbose_name': 'Favourites'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Newsletter Subscribers'},
        ),
        migrations.AlterModelOptions(
            name='phones',
            options={'verbose_name': 'Phones'},
        ),
        migrations.AlterModelOptions(
            name='statesincountry',
            options={'verbose_name': 'States and Countries'},
        ),
        migrations.AlterModelOptions(
            name='topbrand',
            options={'verbose_name': 'Home Page Top Brand'},
        ),
        migrations.AlterModelOptions(
            name='userfilter',
            options={'verbose_name': 'User Filter'},
        ),
        migrations.DeleteModel(
            name='ClickedTOProduct',
        ),
    ]