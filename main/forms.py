from django import forms


class NewsletterForm(forms.Form):
    email = forms.CharField(label='Newsletter', required=False, widget=forms.TextInput(attrs={
    		'placeholder': 'you@gmail.com',
    		'class': 'form-control bg-light small'
    	 }))
