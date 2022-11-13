from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
import pickle
from datetime import datetime


# Create your models here.

class Recommendation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anonymous_user_id = models.CharField(max_length=100, blank=True, null=True)
    recommendation = models.BinaryField(blank=True, null=True)#, serialize=False)#, editable=False) #pickles and stores
    date_added = models.DateTimeField(default=timezone.now, blank=True, null=True)


class Phones(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    phone_image_front = models.ImageField(upload_to='images/', blank=True, null=True)
    phone_image_back = models.ImageField(upload_to='images/', blank=True, null=True)
    phone_image_side = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, unique=True, null=True)
    price = models.FloatField(blank=True, null=True) # in dollar
    network = models.CharField(max_length=100, blank=True, null=True)
    body_form_factor = models.CharField(max_length=100, blank=True, null=True)
    body_color = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)  # in gb to be
    storage = models.CharField(max_length=100, blank=True, null=True)  # in gb to be
    display_resolution = models.CharField(max_length=100, blank=True, null=True)
    main_camera_resolution = models.CharField(max_length=100, blank=True, null=True)
    selfie_camera_resolution = models.CharField(max_length=100, blank=True, null=True)
    battery_capacity = models.CharField(max_length=100, blank=True, null=True)
    battery_duration = models.CharField(max_length=100, blank=True, null=True)
    battery_removable = models.BooleanField(blank=True, null=True)
    wlan = models.BooleanField(blank=True, null=True)
    bluetooth = models.BooleanField(blank=True, null=True)
    gps = models.BooleanField(blank=True, null=True)
    fm_radio = models.BooleanField(blank=True, null=True)
    fingerprint_sensor = models.BooleanField(blank=True, null=True)
    water_resistant = models.BooleanField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Phones'


class Userfilter(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anonymous_user_id = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True) # in dollar
    network = models.CharField(max_length=100, blank=True, null=True)
    body_form_factor = models.CharField(max_length=100, blank=True, null=True)
    body_color = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)  # in gb to be
    storage = models.CharField(max_length=100, blank=True, null=True)  # in gb to be
    display_resolution = models.CharField(max_length=100, blank=True, null=True)
    main_camera_resolution = models.CharField(max_length=100, blank=True, null=True)
    selfie_camera_resolution = models.CharField(max_length=100, blank=True, null=True)
    battery_capacity = models.CharField(max_length=100, blank=True, null=True)
    battery_duration = models.CharField(max_length=100, blank=True, null=True)
    battery_removable = models.BooleanField(blank=True, null=True)
    wlan = models.BooleanField(blank=True, null=True)
    bluetooth = models.BooleanField(blank=True, null=True)
    gps = models.BooleanField(blank=True, null=True)
    fm_radio = models.BooleanField(blank=True, null=True)
    fingerprint_sensor = models.BooleanField(blank=True, null=True)
    water_resistant = models.BooleanField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'User Filter'


class Contact(models.Model):
    # id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=100) 
    msg = models.TextField()  
    attended_to = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email + '  -  ' + self.msg[:50] + '...')

    class Meta:
        verbose_name_plural = 'Contact us'


# class Phones2 -> MODEL:
#     id = Integer, primary_key=True
#     aspect_ratio = String(40)
#     sim_card_size = String(40)
#     bluetooth = Boolean
#     wifi = Boolean
#     nfc = Boolean
#     infrared = Boolean
#     usb = Boolean
#     brand = String(40)
#     year = String(10)
#     availability = String(40)
#     price = String(20)
#     network_2g = String(40)
#     network_3g = String(40)
#     network_4g = String(40)
#     network_5g = String(40)
#     sim_size = String(40)
#     sim_multiple = String(40)
#     body_form_factor = String(40)
#     body_keyboard = String(40)
#     body_height = String(40)
#     body_width = String(40)
#     body_weight = String(40)
#     body_thickness = String(40)
#     body_ip_certificate = String(40)
#     body_color = String(40)
#     body_back_material = String(40)
#     body_frame_material = String(40)
#     os = String(40)
#     os_version = String(40)
#     cpu_freq = String(40)
#     cpu_cores = Integer)
#     chipset = String(40)
#     ram = String(40)
#     storage = String(40)
#     card_slot = String(40)
#     display_resolution = String(40) = String(40)
#     display_density = String(40)
#     display_technology = String(40)
#     display_notch = String(40)
#     display_high_refresh_rate = Boolean
#     display_hdr = Boolean
#     main_camera_resolution = String(40)
#     main_camera_f_number = String(40)
#     main_camera_cameras = String(40)
#     main_camera_ois = Boolean
#     main_camera_telephoto = Boolean
#     main_camera_ultrawide = Boolean
#     main_camera_flash = Boolean
#     main_camera_video = String(40)
#     selfie_camera_resolution = String(40)
#     selfie_camera_dual_camera = Boolean
#     selfie_camera_ois = Boolean
#     selfie_camera_front_flask = Boolean
#     selfie_camera_pop_up_camera = Boolean
#     selfie_camera_under_display = Boolean
#     sensor_accelerometer = Boolean
#     sensor_compass = Boolean
#     sensor_gyro = Boolean
#     sensor_compass = Boolean
#     sensor_proximity = Boolean
#     sensor_heart_rate = Boolean
#     sensor_fingerprint = String(40)
#     wlan = String(40)
#     bluetooth = String(40)
#     gps = Boolean
#     nfc = Boolean
#     infrared = Boolean
#     fm_radio = Boolean
#     usb_type_c = Boolean
#     battery_capacity = String(40)
#     battery_removable = String(40)
#     charging_wired = String(40)
#     charging_wireless = String(40)
#     misc_free_text = String(40)
#     misc_order = String(40)
#     misc_reviewed_only = Boolean
#     new = Boolean
#     description = Text(1000) 
#     name = String(300)
#     price = Float)
#     rating = Integer)
