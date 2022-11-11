from django.contrib import admin
from .models import Phones, Userfilter, Contact, Recommendation

# Register your models here.

admin.site.register(Phones)
admin.site.register(Userfilter)
admin.site.register(Contact)
admin.site.register(Recommendation)

