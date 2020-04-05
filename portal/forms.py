"""
Extracted from <https://testdriven.io/blog/django-custom-user-model/>
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
"""
To use the PhoneNumberField, make sure you've installed the phonenumber_field library with
pip install django-phonenumber-field
Found at <https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models>
"""
#from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from .models import CustomUser

from django.core.validators import RegexValidator

"""
TODO: Ask Human Resources what other forms are able to be completed electronically
"""

class PersonalDetailsForm(forms.Form):
    """
    TODO: Check to see what info Human Resources needs from a personal details form
    """
    first_name = forms.CharField(label='First name', max_length=24, required=True)
    last_name = forms.CharField(label='Last name', max_length=24, required=True)
    #phone_number = PhoneNumberField()  //Check why no module named 'phonenumbers'
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=True) # validators should be a list
    virtual_address = forms.CharField(label='Address', max_length=128, required=False, widget=forms.Textarea)
    post_office_box = forms.CharField(label='P.O. Box', max_length=24, required=False)

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'full_name', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'is_staff', )
