from django.urls import path
from .views import (CreatePhones, CreateFAQs, CreateUser,
	Index, Newsletter, About, FAQs, PrivacyPolicy, TOS, 
        )


app_name = 'main'


urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('faqs/', FAQs.as_view(), name='faqs'),
    path('about/', About.as_view(), name='about'),
    path('privacy-policy/', PrivacyPolicy.as_view(), name='privacy-policy'),
    path('tos/', TOS.as_view(), name='tos'),
    path('newsletter/', Newsletter.as_view(), name='newsletter'),

	# WILL BE REMOVED
    path('create-phone/<int:num>/', CreatePhones.as_view(), name='create-phone'),
    path('create-faqs/', CreateFAQs.as_view(), name='create-faqs'),
    path('create-user/<int:num>/', CreateUser.as_view(), name='create-user'),
]
