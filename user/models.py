from django.db import models
from django.db.models import Q
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
import pickle


# Create your models here.

# help(models.TextField)

class Recommendation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anonymous_user_id = models.CharField(max_length=100, blank=True, null=True)
    recommendation = models.BinaryField(blank=True, null=True)#, serialize=False)#, editable=False) #pickles and stores
    date_added = models.DateTimeField(default=timezone.now, blank=True, null=True)


    # def pickler(self):
    #     self.recommendation = pickle.dumps(recommendation)
    #     return 'Done'

    # def unpickler(self):
    #     recommendation_pickle = self.recommendation
    #     recommendation = pickle.loads(recommendation_pickle)
    #     return recommendation


class Phones(models.Model):
    # id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    phone_image_front = models.FileField(upload_to='images/', blank=True, null=True)
    phone_image_back = models.FileField(upload_to='images/', blank=True, null=True)
    phone_image_side = models.FileField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, unique=True, null=True)
    price = models.FloatField(blank=True, null=True) # in dollar
    # price_min = models.FloatField(blank=True, null=True) # in dollar
    # price_max = models.FloatField(blank=True, null=True) # in dollar

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
    # id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anonymous_user_id = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True) # in dollar
    # price_min = models.FloatField(blank=True, null=True) # in dollar
    # price_max = models.FloatField(blank=True, null=True) # in dollar

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


# class Phones2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     brand
#     year
#     color 
#     storage
#     display_size
#     aspect_ratio
#     network
#     sim_card_size
#     bluetooth = db.Column(db.Boolean)
#     wifi = db.Column(db.Boolean)
#     nfc = db.Column(db.Boolean)
#     infrared = db.Column(db.Boolean)
#     usb = db.Column(db.Boolean)
#     brand = db.Column(db.String(40))
#     year = db.Column(db.String(10))
#     availability = db.Column(db.String(40))
#     price = db.Column(db.String(20))
#     network_2g = db.Column(db.String(40))
#     network_3g = db.Column(db.String(40))
#     network_4g = db.Column(db.String(40))
#     network_5g = db.Column(db.String(40))
#     sim_size = db.Column(db.String(40))
#     sim_multiple = db.Column(db.String(40))
#     body_form_factor = db.Column(db.String(40))
#     body_keyboard = db.Column(db.String(40))
#     body_height = db.Column(db.String(40))
#     body_width = db.Column(db.String(40))
#     body_weight = db.Column(db.String(40))
#     body_thickness = db.Column(db.String(40))
#     body_ip_certificate = db.Column(db.String(40))
#     body_color = db.Column(db.String(40))
#     body_back_material = db.Column(db.String(40))
#     body_frame_material = db.Column(db.String(40))
#     os = db.Column(db.String(40))
#     os_version = db.Column(db.String(40))
#     cpu_freq = db.Column(db.String(40))
#     cpu_cores = db.Column(db.Integer))
#     chipset = db.Column(db.String(40))
#     ram = db.Column(db.String(40))
#     storage = db.Column(db.String(40))
#     card_slot = db.Column(db.String(40))
#     display_resolution = db.Column(db.String(40))
#     display_size = db.Column(db.String(40))
#     display_density = db.Column(db.String(40))
#     display_technology = db.Column(db.String(40))
#     display_notch = db.Column(db.String(40))
#     display_high_refresh_rate = db.Column(db.Boolean)
#     display_hdr = db.Column(db.Boolean)
#     main_camera_resolution = db.Column(db.String(40))
#     main_camera_f_number = db.Column(db.String(40))
#     main_camera_cameras = db.Column(db.String(40))
#     main_camera_ois = db.Column(db.Boolean)
#     main_camera_telephoto = db.Column(db.Boolean)
#     main_camera_ultrawide = db.Column(db.Boolean)
#     main_camera_flash = db.Column(db.Boolean)
#     main_camera_video = db.Column(db.String(40))
#     selfie_camera_resolution = db.Column(db.String(40))
#     selfie_camera_dual_camera = db.Column(db.Boolean)
#     selfie_camera_ois = db.Column(db.Boolean)
#     selfie_camera_front_flask = db.Column(db.Boolean)
#     selfie_camera_pop_up_camera = db.Column(db.Boolean)
#     selfie_camera_under_display = db.Column(db.Boolean)
#     sensor_accelerometer = db.Column(db.Boolean)
#     sensor_compass = db.Column(db.Boolean)
#     sensor_gyro = db.Column(db.Boolean)
#     sensor_compass = db.Column(db.Boolean)
#     sensor_proximity = db.Column(db.Boolean)
#     sensor_heart_rate = db.Column(db.Boolean)
#     sensor_fingerprint = db.Column(db.String(40))
#     wlan = db.Column(db.String(40))
#     bluetooth = db.Column(db.String(40))
#     gps = db.Column(db.Boolean)
#     nfc = db.Column(db.Boolean)
#     infrared = db.Column(db.Boolean)
#     fm_radio = db.Column(db.Boolean)
#     usb_type_c = db.Column(db.Boolean)
#     battery_capacity = db.Column(db.String(40))
#     battery_removable = db.Column(db.String(40))
#     charging_wired = db.Column(db.String(40))
#     charging_wireless = db.Column(db.String(40))
#     misc_free_text = db.Column(db.String(40))
#     misc_order = db.Column(db.String(40))
#     misc_reviewed_only = db.Column(db.Boolean)
#     new = db.Column(db.Boolean)
#     description = db.Column(db.Text(1000)) 
#     name = db.Column(db.String(300))
#     price = db.Column(db.Float)
#     rating = db.Column(db.Integer)
