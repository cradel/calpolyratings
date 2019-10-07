from __future__ import unicode_literals
import requests

from django.utils.translation import pgettext, ugettext, ugettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms


from captcha.fields import ReCaptchaField
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm
from allauth.account.utils import get_user_model, user_username, user_email
from allauth.account.adapter import get_adapter
from allauth.account import app_settings
from authentication.validators import username_checker, check_calpoly_email

from utilities import *


# overridden to add captcha field and clean_captcha() for validation
class MySignupForm(SignupForm):
    #captcha = forms.CharField(required=True)

    def clean_captcha(self):
        return
        if not recaptcha_check(self.cleaned_data['captcha']):
            raise ValidationError('Captcha is required.')
        return self.cleaned_data['captcha']

    def clean_email(self):
        try:
            email = self.cleaned_data.get("email")
            check_calpoly_email(email)
            return email
        except forms.ValidationError as e:
            raise e


# overridden to switch up the error msg for username/pw mismatch
class MyLoginForm(LoginForm):
    #captcha = forms.CharField(required=True)

    def clean_captcha(self):
        return
        if not recaptcha_check(self.cleaned_data['captcha']):
            raise ValidationError('Captcha is required.')
        return self.cleaned_data['captcha']


class MyResetPasswordForm(ResetPasswordForm):
    #captcha = forms.CharField(required=True)

    def clean_captcha(self):
        return
        if not recaptcha_check(self.cleaned_data['captcha']):
            raise ValidationError('Captcha is required.')
        return self.cleaned_data['captcha']
