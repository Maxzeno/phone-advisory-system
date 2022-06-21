from django.urls import path
from .views import Signup, Signin, Signout, ForgotPassword, ResetPassword, ConfirmToken, ConfirmEmail

app_name = 'registration'

urlpatterns = [
    path('signin/', Signin.as_view(), name='login'),
    path('signout/',  Signout.as_view(), name='signout'),
    path('signup/',  Signup.as_view(), name='signup'),
    path('forgot-password/',  ForgotPassword.as_view(), name='forgot-password'),
    path('reset-password/<str:token>/',  ResetPassword.as_view(), name='reset-password'),
    path('confirm-token/<str:user_id>/', ConfirmToken.as_view(), name='confirm-token'),
    path('confirm-email/<str:user_id>/<str:token>/',  ConfirmEmail.as_view(), name='confirm-email'),

]
 