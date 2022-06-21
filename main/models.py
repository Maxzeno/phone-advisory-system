from django.db import models
from django.utils import timezone

# Create your models here.

"""
class About(models.Model): 
    pass

class PrivacyPolicy(models.Model): 
    pass

class TOS(models.Model):   
    pass
"""


class Newsletter(models.Model):       
    # id = models.IntegerField(primary_key=True) 
    email = models.EmailField(max_length=100)
    confirmed_email = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = 'Newsletter Subscribers'


class FAQs(models.Model): 
    # id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.TextField() 
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.question)


    class Meta:
        verbose_name_plural = 'FAQ'
