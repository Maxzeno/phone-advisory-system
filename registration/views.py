from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, models
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .forms import SigninForm, SignupForm, ForgotPasswordForm, ResetPasswordForm
from user.utils import length_favourite, know_anonymous
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


class Signup(View):
	def get(self, request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		logout(request)
		request.session['anonymous_user_id'] = anonymous_user_id
		form = SignupForm()

		return render(request, 'registration/signup.html', {'form':form})

	def post(self, request):
		form = SignupForm(request.POST)

		if form.is_valid():
			email = form.data.get('email')
			username = form.data.get('username')
			password = form.data.get('password')

			user = models.User(email=email, username=username)
			user.set_password(password)
			user.is_active=False
			user.save()

			return redirect(reverse('registration:confirm-token', kwargs={'user_id':user.id}))

		return render(request, 'registration/signup.html', {'form':form})


class ConfirmToken(View):
	def get(self, request, user_id):
		user = models.User.objects.get(id=user_id)
		s = URLSafeTimedSerializer('supersecretwala')
		token = s.dumps(user_id, salt='email-confirm')
		link = request.get_host() + reverse('registration:confirm-email', kwargs={'user_id': user.id, 'token':token})
		html_body = get_template('registration/template_confirm_email.html').render({'confirmation_email': link})
		msg = EmailMultiAlternatives('Confirmation email', f'Your confirmation link  {link}', 'nwaegunwaemmauel@gmail.com', [user.email])
		msg.attach_alternative(html_body, "text/html")
		msg.send()
		# messages.success(request, 'A confirmation email was sent.')
		return render(request, 'registration/status_msg.html', {
				'title':'Confirm email', 
				'msg':'Comfirmation email has been sent.', 
				'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:confirm-token", kwargs={"user_id": user_id}) }">Resend</a>', 
				'l':length_favourite(request)
			})


class ConfirmEmail(View):
	def get(self, request, user_id, token):
		referer = request.META.get('HTTP_REFERER')

		try:
			s = URLSafeTimedSerializer('supersecretwala')
			the_user_id = s.loads(token, salt='email-confirm', max_age=200000)
			user = models.User.objects.get(id=the_user_id)
			user.is_active = True
			user.save()
			return render(request, 'registration/status_msg.html', {
				'title':'Email confirmed', 
				'msg':'Email confirmed you can now.', 
				'action':'<a class="btn btn-success btn-sm w-100" href="/signin/">signin</a>',
				'l':length_favourite(request)
			})
		except SignatureExpired:
			return render(request, 'registration/status_msg.html', {
				'title':'Token expired', 
				'msg':'This Token Has expired.', 
				'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:confirm-token", kwargs={"user_id": user_id}) }">Get New One</a>',
				'l':length_favourite(request)
			})



class Signin(View):
	def get(self, request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		logout(request)
		request.session['anonymous_user_id'] = anonymous_user_id
		request.session['next'] = request.GET.get('next')
		form = SigninForm()
		return render(request, 'registration/signin.html', {'form':form})

	def post(self, request):
		form = SigninForm(request.POST)
		if form.is_valid():
			email = form.data.get('email')
			user = models.User.objects.get(email=email)

			next_url = request.session.pop('next', None)

			if user.is_active:				
				login(request, user)
				know_anonymous(request)
				return redirect(next_url or 'main:index')
			else:
				return redirect(reverse("registration:confirm-token", kwargs={"user_id": user.id}))

		return render(request, 'registration/signin.html', {'form':form})


class ForgotPassword(View):
	def get(self, request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		logout(request)
		request.session['anonymous_user_id'] = anonymous_user_id

		form = ForgotPasswordForm()
		return render(request, 'registration/forgot_password.html', {'form':form})

	def post(self, request):
		form = ForgotPasswordForm(request.POST)
		if form.is_valid():
			user = models.User.objects.filter(email=form.data.get('email')).first()
			if user:
				s = URLSafeTimedSerializer('supersecretwala')
				token = s.dumps(user.id, salt='email-reset')
				link = request.get_host() + reverse('registration:reset-password', kwargs={'token':token})
				html_body = get_template('registration/template_reset_password.html').render({'reset_password': link})
				msg = EmailMultiAlternatives('Confirmation email', f'Your confirmation link  {link}', 'nwaegunwaemmauel@gmail.com', [user.email])
				msg.attach_alternative(html_body, "text/html")
				msg.send()

				return render(request, 'registration/status_msg.html', {
					'title':'Confirm email', 
					'msg':'Comfirmation email has been sent.', 
					'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:forgot-password") }">Try different email</a>', 
					'l':length_favourite(request)
				})

			return render(request, 'registration/status_msg.html', {
					'title':'Confirm email', 
					'msg':'Comfirmation email has been sent.', 
					'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:forgot-password") }">Try different email</a>', 
					'l':length_favourite(request)
				})
		return render(request, 'registration/forgot_password.html', {'form':form})



class ResetPassword(View):
	def get(self, request, token):
		try:
			s = URLSafeTimedSerializer('supersecretwala')
			the_user_id = s.loads(token, salt='email-reset', max_age=200000)
			form =  ResetPasswordForm()
			return render(request, 'registration/reset_password.html', {'form':form, 'l':length_favourite(request)})

		except SignatureExpired:
			return render(request, 'registration/status_msg.html', {
				'title':'Token expired', 
				'msg':'This Token Has expired.', 
				'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:forgot-password") }">Get New One</a>',
				'l':length_favourite(request)
			})

	def post(self, request, token):
		try:
			form =  ResetPasswordForm(request.POST)
			s = URLSafeTimedSerializer('supersecretwala')
			if form.is_valid():
				the_user_id = s.loads(token, salt='email-reset', max_age=200000)
				user = models.User.objects.get(id=the_user_id)
				user.set_password(form.data.get('password'))
				user.save()
				return render(request, 'registration/status_msg.html', {
					'title':'Email confirmed', 
					'msg':'Email confirmed you can now.', 
					'action':'<a class="btn btn-success btn-sm w-100" href="/signin/">signin</a>',
					'l':length_favourite(request)
				})
			return render(request, 'registration/reset_password.html', {'form':form, 'l':length_favourite(request)})

		except SignatureExpired:
			return render(request, 'registration/status_msg.html', {
				'title':'Token expired', 
				'msg':'This Token Has expired.', 
				'action':f'<a class="btn btn-success btn-sm w-100" href="{ reverse("registration:forgot-password") }">Get New One</a>',
				'l':length_favourite(request)
			})


class Signout(View):
	def get(self, request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		logout(request)
		request.session['anonymous_user_id'] = anonymous_user_id
		return redirect('main:index')

