from django import forms
from .models import Phones
from .utils import choice_field_tuple, EmmaCustomSelect, ButtonInput

# print(help(forms.ModelChoiceField))



class FullNameForm(forms.Form):
    first_name = forms.CharField(label='First name', required=False, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    last_name = forms.CharField(label='Last name', required=False, widget=forms.TextInput(attrs={'placeholder': 'name'}))


class ContactForm(forms.Form):
    email = forms.CharField(label='Email', required=False, widget=forms.TextInput(attrs={'placeholder': 'you@mail.com'}))
    message = forms.CharField(label='Message', required=False, widget=forms.Textarea(attrs={
    	'placeholder':'The Message',
    	'rows':'5',
    	}))


# class PersonalInfomationForm(forms.Form):
#     first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
#     last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
#     phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
#     gender = forms.ChoiceField(label='Gender', choices=(('gender', 'Gender'), ('male', 'Male'), ('female', 'Female'), ('complicated', 'Complicated')))   
#     country = forms.ChoiceField(label='Country', choices=()) 
#     state = forms.ChoiceField(label='State', choices=())     
#     city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder': 'Your City'}))
#     address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Where you live'}))


class PhoneForm(forms.Form):
    # name = forms.ModelChoiceField(Phones.objects.all(), required=False)#, widget=EmmaCustomSelect())
    brand = forms.ChoiceField(choices=choice_field_tuple('brand', '-'*8), required=False)
    year = forms.ChoiceField(choices=choice_field_tuple('year', '-'*8), required=False)
    price = forms.FloatField(label='Budget', required=False)
    # price_min = forms.FloatField(label='Price min', required=False)
    # price_max = forms.FloatField(label='Price max', required=False)
    network = forms.ChoiceField(choices=choice_field_tuple('network', '-'*8), required=False)
    body_form_factor = forms.ChoiceField(choices=choice_field_tuple('body_form_factor', '-'*8), required=False)
    body_color = forms.ChoiceField(choices=choice_field_tuple('body_color', '-'*8), required=False)
    os = forms.ChoiceField(choices=choice_field_tuple('os', '-'*8), required=False)
    ram = forms.ChoiceField(choices=choice_field_tuple('ram', '-'*8), required=False)
    storage = forms.ChoiceField(choices=choice_field_tuple('storage', '-'*8), required=False)
    display_resolution = forms.ChoiceField(choices=choice_field_tuple('display_resolution', '-'*8), required=False)
    main_camera_resolution = forms.ChoiceField(choices=choice_field_tuple('main_camera_resolution', '-'*8), required=False)
    selfie_camera_resolution = forms.ChoiceField(choices=choice_field_tuple('selfie_camera_resolution', '-'*8), required=False)
    battery_capacity = forms.ChoiceField(choices=choice_field_tuple('battery_capacity', '-'*8), required=False)
    battery_duration = forms.ChoiceField(choices=choice_field_tuple('battery_duration', '-'*8), required=False)

    battery_removable = forms.BooleanField(required=False)
    wlan = forms.BooleanField(required=False)
    bluetooth = forms.BooleanField(required=False)
    gps = forms.BooleanField(required=False)
    fm_radio = forms.BooleanField(required=False)
    fingerprint_sensor = forms.BooleanField(required=False)
    water_resistant = forms.BooleanField(required=False)


class SearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone name',
            'class': 'py-0 my-0 form-control bg-light border-0 small'
        }))


