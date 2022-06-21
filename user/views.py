from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse
from user import models
from .models import Q
from user import forms
from .utils import Filter, length_favourite, range_dict
from .forms import ContactForm, FullNameForm
from django.contrib import messages
import os
import json
import math
from urllib.parse import urlencode
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from registration.forms import ResetPasswordForm

# Create your views here.

class Discover(Filter, View):
	template = 'user/discover.html'
	extra_context = {}

	def get(self, request):
		data = dict(request.GET)
		data.pop('csrfmiddlewaretoken', False)
		data.pop('page', False)

		form = forms.PhoneForm(request.GET)

		page = request.GET.get('page')
		active_page = int(page) if page != None else 1
		lm = 16

		searchform = forms.SearchForm(request.GET)
		name = searchform.data.get('name')

		if searchform.is_valid and name:
			query = {'query_str': 'Q()', 'params': f'&name={name}', 'filter_data': {}}

			matched_phones = models.Phones.objects.filter(name__contains=name.lower().strip().replace('  ', ' ')).all()
			phones = matched_phones[lm*(active_page-1): lm*active_page]
			l = len(matched_phones)
			reset_msg = 'Reset Search'
			in_process = 'Search'
		else:
			query = self.process(request.GET)
			query_str = query['query_str'] if query['query_str'] != 'Q()' else 'Q()'
			phone_data = self.recom(request, query_str, query['filter_data'], lm, active_page)

			phones = phone_data[0]
			l = phone_data[1]
			reset_msg = 'Reset Filter'
			in_process = 'Results'

		pages = math.ceil(l / lm) 

		dct = range_dict(active_page, pages)

		favourite = request.COOKIES.get('favourite')
		if favourite:
			lst_favourite = [ int(i) for i in json.loads(favourite) ]
		else:
			lst_favourite = []

		# if query['filter_data']:
		# 	self.userfilter(request, query['filter_data'])


		filter_data = query['filter_data']
		filter_data.pop('user_id', False)
		params = query['params']


		context = {
			'dct': dct, 'phones': phones, 'pages': pages, 'active_page': active_page, 'lst_favourite': lst_favourite, 
			'l': len(lst_favourite), 'params': query['params'], 'form': form, 
			'rang': range(dct['range_start'], dct['range_stop']), 'searchform': searchform,
			'filter': bool(params), 'reset_msg': reset_msg, 'in_process': in_process,
			**self.extra_context
		}
		return render(request, self.template, context)
		


# if params:
# 	cookie.set_cookie('filter', value=json.dumps(filter_data), max_age=1000000)
# 	cookie.set_cookie('params', value=params, max_age=1000000)
# 	cookie.set_cookie('query_str', value=query_str, max_age=1000000)

# # key, value='', max_age=None, expires=None, path='/',
# #                domain=None, secure=False, httponly=False, samesite=None):


# return cookie



class Resetter(View):
	def get(self, request, redirect_url=''):
		return redirect('/'+redirect_url+'/')



class Favourite(View):
	def get(self, request):
		favourite = request.COOKIES.get('favourite')
		if favourite:
			lst_favourite = [ int(i) for i in json.loads(favourite) ]
		else:
			lst_favourite = []

		phones = models.Phones.objects.filter(id__in=lst_favourite).all()
		context = {'lst_favourite':lst_favourite, 'phones':phones, 'l':len(lst_favourite)}
		return render(request, 'user/favourite.html', context)


class Settings(View):
	def get(self, request):
		return render(request, 'user/settings.html', {'l':length_favourite(request)})


class Contact(View):
	def get(self, request):
		form = ContactForm()
		return render(request, 'user/contact.html', {'form':form, 'l':length_favourite(request)})

	def post(self, request):
		form = ContactForm(request.POST)
		if form.is_valid():
			msg = models.Contact.objects.create(email=form.data.get('email'), msg=form.data.get('message'))
			messages.success(request, 'Message received')
			return redirect(reverse('user:contact'))
		return render(request, 'user/contact.html', {'form':form, 'l':length_favourite(request)})


class FullName(View):
	def get(self, request):
		first_name = request.user.first_name
		last_name = request.user.last_name

		form = FullNameForm({'first_name': first_name, 'last_name': last_name})

		return render(request, 'user/fullname.html', {'form':form, 'l':length_favourite(request)})

	def post(self, request):
		form = FullNameForm(request.POST)
		if form.is_valid():
			data = dict(request.POST)
			data.pop('csrfmiddlewaretoken', False)
			user = User.objects.filter(pk=request.user.pk).update(first_name=data.get('first_name')[0], last_name=data.get('last_name')[0])
			messages.success(request, 'Full name updated')
			return redirect(reverse('user:settings'))
		return render(request, 'user/fullname.html', {'form':form, 'l':length_favourite(request)})


class Security(View):
	def get(self, request):
		s = URLSafeTimedSerializer('supersecretwala')
		token = s.dumps(request.user.id, salt='email-reset')
		link = request.get_host() + reverse('user:security-reset-password', kwargs={'token':token})

		html_body = get_template('user/template_reset_password.html').render({'reset_password': link})
		msg = EmailMultiAlternatives('Confirmation email', f'Your confirmation link  {link}', 'nwaegunwaemmauel@gmail.com', ['mmnlchidera@gmail.com'])
		msg.attach_alternative(html_body, "text/html")
		msg.send()
		messages.success(request, 'A confirmation email was sent.')
		return redirect(reverse('user:settings'))


class SecurityResetPassword(View):
	def get(self, request, token):
		try:
			s = URLSafeTimedSerializer('supersecretwala')
			user_id = s.loads(token, salt='email-reset', max_age=200000)
			form =  ResetPasswordForm()
			return render(request, 'user/security_reset_password.html', {'form':form, 'l':length_favourite(request)})

		except SignatureExpired:
			return HttpResponse('All bad')

	def post(self, request, token):
		try:
			form =  ResetPasswordForm(request.POST)
			s = URLSafeTimedSerializer('supersecretwala')
			if form.is_valid():
				user_id = s.loads(token, salt='email-reset', max_age=200000)
				user = User.objects.filter(id=user_id).first()
				user.set_password(form.data.get('password'))
				user.save()
				messages.success(request, 'Password reset successfull.')
				return redirect(reverse('user:settings'))
			return render(request, 'user/security_reset_password.html', {'form':form, 'l':length_favourite(request)})

		except SignatureExpired:
			return HttpResponse('All bad')

