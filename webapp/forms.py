from django import forms
from .models import Subscription



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['username', 'email']


class RegisterUserForm(forms.Form):
    email = forms.EmailField(label='Email')
