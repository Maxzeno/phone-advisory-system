# Generated by Django 3.0.8 on 2022-11-07 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.TextField()),
                ('attended_to', models.BooleanField(default=False)),
                ('resolved', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Contact us',
            },
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_image_front', models.FileField(blank=True, null=True, upload_to='images/')),
                ('phone_image_back', models.FileField(blank=True, null=True, upload_to='images/')),
                ('phone_image_side', models.FileField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('body_form_factor', models.CharField(blank=True, max_length=100, null=True)),
                ('body_color', models.CharField(blank=True, max_length=100, null=True)),
                ('os', models.CharField(blank=True, max_length=100, null=True)),
                ('ram', models.CharField(blank=True, max_length=100, null=True)),
                ('storage', models.CharField(blank=True, max_length=100, null=True)),
                ('display_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('main_camera_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('selfie_camera_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_removable', models.BooleanField(blank=True, null=True)),
                ('wlan', models.BooleanField(blank=True, null=True)),
                ('bluetooth', models.BooleanField(blank=True, null=True)),
                ('gps', models.BooleanField(blank=True, null=True)),
                ('fm_radio', models.BooleanField(blank=True, null=True)),
                ('fingerprint_sensor', models.BooleanField(blank=True, null=True)),
                ('water_resistant', models.BooleanField(blank=True, null=True)),
                ('date_added', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name_plural': 'Phones',
            },
        ),
        migrations.CreateModel(
            name='Userfilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('body_form_factor', models.CharField(blank=True, max_length=100, null=True)),
                ('body_color', models.CharField(blank=True, max_length=100, null=True)),
                ('os', models.CharField(blank=True, max_length=100, null=True)),
                ('ram', models.CharField(blank=True, max_length=100, null=True)),
                ('storage', models.CharField(blank=True, max_length=100, null=True)),
                ('display_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('main_camera_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('selfie_camera_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('battery_removable', models.BooleanField(blank=True, null=True)),
                ('wlan', models.BooleanField(blank=True, null=True)),
                ('bluetooth', models.BooleanField(blank=True, null=True)),
                ('gps', models.BooleanField(blank=True, null=True)),
                ('fm_radio', models.BooleanField(blank=True, null=True)),
                ('fingerprint_sensor', models.BooleanField(blank=True, null=True)),
                ('water_resistant', models.BooleanField(blank=True, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Filter',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendation', models.BinaryField(blank=True, null=True)),
                ('date_added', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
