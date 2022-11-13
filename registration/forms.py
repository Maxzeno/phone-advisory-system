from django.shortcuts import redirect
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, models
from django.contrib import messages


class SigninForm(forms.Form):
	email = forms.EmailField(required=False, max_length=100, widget=forms.TextInput(attrs={
		'placeholder':'you@gmail.com',
	}))

	password = forms.CharField(required=False, max_length=32, widget=forms.PasswordInput(attrs={
		'placeholder':'your password',
	}))

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		user = User.objects.filter(email=email).first()

		if user:
			is_auth = user.check_password(password)
			# is_auth2 = authenticate(username=user.username, password=password)
			if is_auth:
				return email
			raise forms.ValidationError('Invalid Login')

		raise forms.ValidationError('Invalid Login')


class SignupForm(forms.Form):
	username = forms.CharField(required=False, max_length=100,  widget=forms.TextInput(attrs={
		'placeholder':'your username',
		}))
	email = forms.EmailField(required=False, max_length=100,  widget=forms.EmailInput(attrs={
		'placeholder':'you@gmail.com',
		}))
	password = forms.CharField(required=False, max_length=128, widget=forms.PasswordInput(attrs={
		'placeholder':'your password',
		}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		found_username = User.objects.filter(username=username.lower()).first()
		if found_username:
			raise forms.ValidationError('Username Exist')
		return username.lower()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		found_email = User.objects.filter(email=email.lower()).first()
		if found_email:
			raise forms.ValidationError('Email Exist')
		return email.lower()


	def clean_password(self):
		password = self.cleaned_data.get('password')
		if len(password) < 8 or len(password) > 128:
			if len(password) < 8:
				raise forms.ValidationError('Password should be greater than 7 characters')
			raise forms.ValidationError('Password should be less than 129 characters')

		elif password.isnumeric() or password.isalpha():
			raise forms.ValidationError('Password should contain alphabets and numbers')

		return password
            

class ForgotPasswordForm(forms.Form):
	email = forms.EmailField(required=False, max_length=100, widget=forms.TextInput(attrs={
		'placeholder':'you@gmail.com',
		}))


class ResetPasswordForm(forms.Form):
	password = forms.CharField(label='Password', required=False, max_length=100, widget=forms.PasswordInput(attrs={
		'placeholder':'new password',
		}))

	confirm_password = forms.CharField(label='Confirm', required=False, max_length=100, widget=forms.PasswordInput(attrs={
		'placeholder':'confirm password',
		}))

	def clean_password(self):
		password = self.cleaned_data.get('password')

		if len(password) < 8 or len(password) > 128:
			if len(password) < 8:
				raise forms.ValidationError('Password should be greater than 7 characters')
			raise forms.ValidationError('Password should be less than 129 characters')

		elif password.isnumeric() or password.isalpha():
			raise forms.ValidationError('Password should contain alphabets and numbers')

		return password

	def clean_confirm_password(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')

		if password and password != confirm_password:
			raise forms.ValidationError('The Two Passwords Don\'t match')

		return confirm_password
            




