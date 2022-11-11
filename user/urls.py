from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
	Discover, Favourite, Settings, Contact, Resetter, FullName,
	Security, SecurityResetPassword,
	)


app_name = 'user'


urlpatterns = [
    path('discover/', Discover.as_view(), name='discover'),
    path('favourite/', Favourite.as_view(), name='favourite'),
    path('settings/', login_required(Settings.as_view()), name='settings'),
    path('contact/', Contact.as_view(), name='contact'),
    path('resetter/', Resetter.as_view(), name='resetter-home'),
    path('resetter/<str:redirect_url>/', Resetter.as_view(), name='resetter'),
    path('settings/fullname/', login_required(FullName.as_view()), name='settings-fullname'),
    path('security/', login_required(Security.as_view()), name='security'),
    path('security-reset-password/<str:token>/', login_required(SecurityResetPassword.as_view()), name='security-reset-password'),

]
