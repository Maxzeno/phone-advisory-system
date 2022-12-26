from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse
from django.contrib import messages
from user import models
from .models import Newsletter as NewsletterModel, FAQs as FAQsModel
import os
import json
import math
from user import forms
from .forms import NewsletterForm
from user.models import Q, Phones
from user.utils import Filter, length_favourite, randomise, range_dict, name_phone_and_brand
from user.views import Discover
import csv


class Index(Discover):
	template = 'main/index.html'
	extra_context = {'newsletterForm': NewsletterForm()}

	
class Newsletter(View):
	def post(self, request):
		form = NewsletterForm(request.POST)
		from_path = request.META.get('HTTP_REFERER')
		newsletter_sub = form.data.get('email')
		found = NewsletterModel.objects.filter(email=newsletter_sub).first()
		if found:
			if found.active == False:
				found.active = True
				found.save()
				messages.success(request, 'Activated Newsletter')
				return redirect(from_path or reverse('main:index'))
				
			else:
				messages.success(request, 'Already Subscribed to Newsletter')
				return redirect(from_path or reverse('main:index'))

		sub = NewsletterModel.objects.create(email=newsletter_sub)
		messages.success(request, 'Subscribed to Newsletter')
		return redirect(from_path or reverse('main:index'))

class About(View):
	def get(self, request):
		return render(request, 'main/about.html', {
			'l': length_favourite(request)})


class FAQs(View):
	def get(self, request):
		page = request.GET.get('page')
		active_page = int(page) if page != None else 1

		lm = 10
		off = (int(page)-1)*lm  if page != None else 0

		l = FAQsModel.objects.count()
		pages = math.ceil(l / lm) 

		dct = range_dict(active_page, pages)
		faqs = FAQsModel.objects.order_by('date_added').reverse()[off: lm*active_page]
		return render(request, 'main/faqs.html', {
			'dct': dct, 'pages': pages, 'active_page': active_page,
			'rang': range(dct['range_start'], dct['range_stop']),
			'faqs': faqs,
			'l': length_favourite(request)})


class PrivacyPolicy(View):
	def get(self, request):
		return render(request, 'main/privacy_policy.html', {
			'l': length_favourite(request)})


class TOS(View):
	def get(self, request):
		return render(request, 'main/tos.html', {
			'l': length_favourite(request)})


""" WILL BE REMOVED (USED TO AUTO ADD FAQS) """
class CreateFAQs(View):
	def get(self, request):
		questions = ['Why Can\'t i login?', 'My filters is not reflecting?', 'My search is not woeking', 'i can\'t change my country', 'why does location icon say none']
		answers = ['''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''] * 5

		for i in range(len(questions)):
			faqs = FAQsModel.objects.create(question=questions[i], answer=answers[i])
		return HttpResponse('done creating FAQs')
			

""" WILL BE REMOVED (USED TO AUTO ADD PHONES) """
class CreatePhones(View):
	def get(self, request, num):
		price = [200, 365, 155, 2036, 88, 96, 567, 211, 96]
		images_list = ['img/51vf1R1wS9L._AC_UY218__gfuauf.jpg', 'img/71DCZOdq92S._AC_UY218__1_eckyyu.jpg', 'img/71RxOftVoQL._AC_UY218__cmgsmo.jpg', 'img/190_uta7bp.jpg']
		# images_list = ['img/51vf1R1wS9L._AC_UY218_.jpg', 'img/71DCZOdq92S._AC_UY218_ (1).jpg', 'img/71RxOftVoQL._AC_UY218_.jpg', 'img/618LuqyIX6L._AC_UY218_.jpg']
		phone_image_front = images_list
		phone_image_back = images_list
		phone_image_side = images_list
		# description = ['LG Stylo 6 (64GB, 4GB) 6.8", w/Built-in Stylus Pen, 4000mAh Battery, 4G LTE GSM T-Mobile Unlocked (AT&T, Metro, Straight Talk)',
		# 'Samsung Galaxy A12 (A127F) 128GB Dual SIM, GSM Unlocked, (CDMA Verizon/Sprint Not Supported) Smartphone International Version',
		# 'Google Pixel 6 Pro - 5G Android Phone - Unlocked Smartphone with Advanced Pixel Camera and Telephoto Lens - 128GB - Stormy Black',
		# 'Nokia G50 5G | Android 11 | Unlocked Smartphone | US Version | 4/128GB | 6.82-Inch Screen | 48MP Triple Camera | Ocean Blue',
		# 'Samsung Galaxy A12 (64GB, 4GB) 6.5" HD+, Quad Camera, 5000mAh Battery, Dual SIM GSM Unlocked Global 4G Volte (T-Mobile, AT&T, Metro)',
		# 'SAMSUNG Galaxy S20 FE 5G Factory Unlocked Android Cell Phone 128GB US Version Smartphone Pro-Grade Camera 30X Space Zoom Night Mode, Cloud Navy',
		# 'OnePlus Nord N100 Midnight Frost Unlocked Smartphone​, 4GB+64GB, US Version, Model BE2011',
		# 'Moto G Power | 2021 | 3-Day battery | Unlocked | Made for US by Motorola | 3/32GB | 48MP Camera | Silver',
		# 'Blackview Android Phone, A80, 4G Dual sim Cell Phones, Bundle Android 10 OS 2GB+16GB ROM Unlocked Blackview Smartphones, 6.21in HD+',
		# 'Latest Android 11 Phone, Ulefone Note 6 Unlocked Smartphone, 6.1” HD+ Full Screen, Quad-core 1GB+32GB Mobile Phone, 3300mAh']

		als = ['pro', 'ultra', 'max', 'mini', 'lite', 'pro max', 'core', '', 'uni', 'i core', 'smart', 'turbo', 'note', 'hot']
		nums = ['12', '10', '18', '102', '20', '15', '50', '43', '22', '190', '6', '1', '30', '1053', '455']

		# name = ['Iphone 12', 'Samsung s22 ultra', 'Itel p32', 'Geonee f102', 'Google pixel 6', 'Iphone 13 pro max', 'Samsung a2 core']
		brand = ['Apple', 'Samsung', 'Tecno', 'Itel', 'Infinix', 'Gionee', 'Google', 'Xiaoma', 'OPPO',
		 'Nokia', 'Vivo', 'Sony', 'ZTE', 'Motorola', 'OnePlus', 'Alcatel', 'Acer']
		year = ['2012', '2015', '1999', '2007', '2022', '2020', '2014']
		network = ['2g', '3g', '4g']
		body_form_factor = ['bar', 'flip', 'slider']
		body_color = ['red', 'green', 'blue', 'orange', 'gold', 'silver', 'mixed', 'cyan']
		os = ['android', 'ios', 'windows']
		ram = ['0.5gb', '1gb', '2gb', '4gb', '8gb']
		storage = ['4gb', '8gb', '16gb', '32gb', '64gb']
		display_resolution = ['1280 x 1024', '1600 x 1200', '1680 x 1050', '1440 x 720', '2240 x 1448', '2440 x 1540']
		main_camera_resolution = ['4mp', '8mp', '12mp', '14mp', '16mp', '20mp']
		selfie_camera_resolution = ['4mp', '8mp', '12mp', '14mp', '16mp', '20mp']
		wlan = [True, False]
		bluetooth = [True, False]
		gps = [True, False]
		fm_radio = [True, False]
		battery_capacity = ['1000mah', '2000mah', '3000mah', '4000mah', '5000mah']
		battery_duration = ['24hours', '48hours', '36hours']
		battery_removable = [True, False]
		fingerprint_sensor = [True, False]
		water_resistant = [True, False]


		for _ in range(int(num)):
			try:
				p_and_b = name_phone_and_brand(brand, als, nums)	
				models.Phones.objects.create(
					price = randomise(price),
					phone_image_front = randomise(phone_image_front),
					phone_image_back = randomise(phone_image_back),
					phone_image_side = randomise(phone_image_side),
					# description = randomise(description),
					name = p_and_b[1].lower(),
					brand = p_and_b[0].lower(),
					year = randomise(year),
					network = randomise(network),
					body_form_factor = randomise(body_form_factor),
					body_color = randomise(body_color),
					os = randomise(os),
					ram = randomise(ram),
					storage = randomise(storage),
					display_resolution = randomise(display_resolution),
					main_camera_resolution = randomise(main_camera_resolution),
					selfie_camera_resolution = randomise(selfie_camera_resolution),
					wlan = randomise(wlan),
					bluetooth = randomise(bluetooth),
					gps = randomise(gps),
					fm_radio = randomise(fm_radio),
					battery_capacity = randomise(battery_capacity),
					battery_duration = randomise(battery_duration),
					battery_removable = randomise(battery_removable),
					fingerprint_sensor = randomise(fingerprint_sensor),
					water_resistant = randomise(water_resistant),
				)
			except:
				continue
		return HttpResponse('done creating')


""" WILL BE REMOVED (USED TO AUTO ADD USERS) """
class CreateUser(View):
	def get(self, request, num):
		email = 'qw%d@gmail.com'
		username = 'qw%d'
		password = 'emmanueZ@9'

		num_in_db = models.User.objects.count()

		for i in range(num_in_db+1, num_in_db+num+1):
			user = models.User(email=email%i, username=username%i)
			user.set_password(password)
			user.save()
		return HttpResponse('done creating users')
